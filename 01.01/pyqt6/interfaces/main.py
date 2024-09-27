import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()
        self.app = app
        self.setWindowTitle("My App")
        # self.setWindowIcon("icon.png")
        self.button = QPushButton("Click me!", self)
        self.InitUI()
    
    def InitUI(self):
        self.setCentralWidget(self.button)
        self.setGeometry(300, 300, 300, 200)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("button clicked")
        dialog = QDialog(self)
        dialog.setWindowTitle("Hello")
        dialog.setGeometry(300, 300, 300, 200)
        dialog.show()
        dialog.exec()
