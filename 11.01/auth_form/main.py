import sys
import mysql.connector

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QWidget, QDialog

cnx = mysql.connector.connect(user= "root", password = "", host= "localhost",database = "db")
print(cnx)
cursor = cnx.cursor()



class PasswordWindow(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100,100,300,150)
        layout = QVBoxLayout()
        self.username_label = QLabel("Имя пользователя:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.check_password)
        self.regist_button = QPushButton("Зарегестрироваться")
        self.regist_button.clicked.connect(self.regist)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.regist_button)
        self.setLayout(layout)

    def check_password(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_found = False
        for user in users:
            if username == user.username and password == user.password:
                user_found = True
                self.close()
                role = user.role
                if role == "role1":
                    window = Window1()
                elif role == "role2":
                    window = Window2()
                window.show()
                break
        if not user_found:
            # Handle the case where no user is found
            # You can display an error message or take other actions here
            print("Invalid username or password")

    def regist(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_found = False
        if not user_found:
            cnx.cursor().execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            cnx.commit()
            self.regist_button.text("Вы зарегестрировались")
        else:
            print("Пользователь уже существует")



class Window1(QWidget):
    def init(self):
        super().init()
        new_window = QDialog(self)
        new_window.setWindowTitle('Окно для пользователя 1')
        new_window.setGeometry(200,200,300,150)
        new_window.exec()



class Window2(QWidget):
    def init(self):
        super().init()
        new_window = QDialog(self)
        new_window.setWindowTitle('Окно для пользователя 2')
        new_window.setGeometry(200,200,300,150)
        new_window.exec()

cnx.cursor().execute("INSERT INTO users (name, password) VALUES (%s, %s)", ("user1", "password1"))
users= cnx.cursor().execute("SELECT name FROM users")
print(users)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PasswordWindow()
    main_window.show()
    sys.exit(app.exec())