from PyQt6.QtWidgets import QTableWidget, QMainWindow, QMenu, QTableWidgetItem, QInputDialog
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize
from db.models.user import User

class DBWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('База данных')
        self.setFixedSize(QSize(800, 600))
        self.createMenu()
        self.createTable()

    def createMenu(self):
        menu = self.menuBar().addMenu('Меню')
        exitAction = QAction('Выход', self)
        exitAction.triggered.connect(self.close)
        updateAction = QAction('Обновить', self)
        updateAction.triggered.connect(lambda: self.showUsers(l=100, p=1))
        createNewAction = QAction('Добавить запись', self)
        createNewAction.triggered.connect(self.createNewRecord)
        deleteAction = QAction('Удалить запись', self)
        deleteAction.triggered.connect(self.deleteRecord)
        menu.addAction(updateAction)
        menu.addAction(createNewAction)
        menu.addAction(deleteAction)
        menu.addAction(exitAction)

    def createTable(self):
        self.table = QTableWidget()
        self.setCentralWidget(self.table)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.itemDoubleClicked.connect(self.editItem)
        self.showUsers()

    def createNewRecord(self):
        user = User(self.db)
        user.Migrate()
        username, ok1 = QInputDialog.getText(self, 'Введите имя', 'Введите имя:')
        if not ok1:
            return
        date, ok2 = QInputDialog.getText(self, 'Введите дату рождения', 'Введите дату рождения:(формат yyyy-MM-dd)')
        if not ok2:
            return
        bio, ok3 = QInputDialog.getMultiLineText(self, 'Введите биографию', 'Введите биографию:')
        if not ok3:
            return
        age, ok4 = QInputDialog.getInt(self, 'Введите возраст', 'Введите возраст:', 18, 1, 100)
        if not ok4:
            return
        phone, ok5 = QInputDialog.getText(self, 'Введите телефон', 'Введите телефон:')
        if not ok5:
            return
        role, ok6 = QInputDialog.getItem(self, 'Выберите роль', 'Выберите роль:', ['user', 'db', 'chart'], 0, False)
        if not ok6:
            return
        passwd, ok7 = QInputDialog.getText(self, 'Введите пароль', 'Введите пароль:')
        if not ok7:
            return
        user.Create(username, date, bio, age, phone, role, passwd)
        self.showUsers()

    def deleteRecord(self):
        id, ok = QInputDialog.getInt(self, 'Введите ID', 'Введите ID:', 1, 1, 100)
        if ok:
            user = User(self.db)
            user.Delete(id)
            self.showUsers()

    def editItem(self, item):
        row = item.row()
        col = item.column()
        menu = QMenu()
        editAction = QAction('Редактировать', self)
        editAction.triggered.connect(lambda: self.editField(row, col))
        editAction.triggered.connect(lambda: self.editUser(row))
        menu.addAction(editAction)
        menu.exec(self.mapToGlobal(item.tableWidget().visualItemRect(item).bottomLeft()))

    def editField(self, row, col):
        item = self.table.item(row, col)
        text, ok = QInputDialog.getText(self, 'Редактирование', f'Введите новое значение для {item.text()}')
        if ok:
            fields = ['id', 'username', 'date', 'bio', 'age', 'role', 'phone']
            user_id = self.table.item(row, 0).text()
            field = fields[col]
            user = User(self.db)
            user.Read(user_id)
            setattr(user, field, text)
            user.Update(user_id, **{field: text})
            self.table.setItem(row, col, QTableWidgetItem(text))

    def showUsers(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Username', 'DateBirth', 'Bio', 'Age', 'Role', 'Phone'])
        users = User(self.db).GetList()
        for i, user in enumerate(users):
            self.table.insertRow(i)
            for j, value in enumerate([user.id, user.username, user.dateBirth, user.bio, user.age, user.role, user.phone]):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

    def editUser(self, row):
        user = User(self.db)
        user.Read(row)
        values = [user.username, user.dateBirth, user.bio, str(user.age), user.role, user.phone]
        text = ','.join(value for value in values if value is not None)
        user.Update(row, *text.split(','))
        self.showUsers()

