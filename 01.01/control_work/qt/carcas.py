from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from PyQt6.QtCore import QSize
from db.models.user import User
from qt.chart import ChartWindow
from qt.db import DBWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self, db, rtxt="nil"):
        super().__init__()
        self.setWindowTitle("cwork")
        self.db = db
        self.setFixedSize(QSize(150, 100))

        self.runtimeText = rtxt
        self.barstatus = QLabel(self)
        self.barstatus.move(5, 5)
        self.barstatus.setStyleSheet("font-size: 16pt;")
        self.barstatus.setText(self.runtimeText)
        self.setCentralWidget(self.barstatus)
        self.initUI()

    def initUI(self):
        match self.runtimeText:
            case "auth":
                self.authEvent(None)
            case "chart":
                self.showChartEvent(None)
            case "db":
                self.dbEvent(None)

    def barStatus(self, txt):
        self.barstatus.setText(txt)
    # ? This method is called when the window wtd to be closed
    def closeEvent(self, event):
        print("close")
        event.accept()
        sys.exit(0)


    # ! AUTH namespace
    # ? This method is called when user need auth(I don`t wanna realise keyfile-tokens, thats cause its runtimed`)
    def authEvent(self, event=None):
        print("auth")
        if event is not None:
            event.accept()

        self.authWindow = QWidget()
        layout = QVBoxLayout()
        self.authWindow.setLayout(layout)

        self.loginEdit = QLineEdit()
        layout.addWidget(self.loginEdit)

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.passwordEdit)

        loginButton = QPushButton("Login")
        loginButton.clicked.connect(self.checkAuth)
        layout.addWidget(loginButton)

        self.authWindow.show()

    def checkAuth(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        print(f"login: {login}, password: {password}")
        user = User(self.db)
        if user.Read(username=login) and user.passwd == password:
            self.authWindow.close()
            self.barStatus("OK")
            self.runtimeText = f"{user.role}"
            self.barStatus(f"({user.role})")
            self.initUI()
        else:
            self.authWindow.close()
            self.barStatus("Wrong")
            self.initUI()


    # ! SHOWCHART namespace
    # ? This method is called when the user wants to see the chart
    def showChartEvent(self, event=None):
        print("chart")
        if event is not None:
            event.accept()

        self.chartWindow = ChartWindow()        
        self.chartWindow.show()


    # ! DB namespace
    # ? This method is called when the user wants to see the database
    def dbEvent(self, event=None):
        print("db")
        if event is not None:
            event.accept()
        self.dbWindow = DBWindow(self.db)
        self.dbWindow.show()

# * Initialize the app and window
def init_app(db, rtxt):
    app = QApplication(sys.argv)
    window = MainWindow(db, rtxt)
    window.show()
    app.exec()

    return app, window