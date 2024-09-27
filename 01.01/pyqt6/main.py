import sys
from PyQt6.QtWidgets import QApplication
from interfaces.main import MainWindow as mw

def main():
    app = QApplication(sys.argv)
    window = mw(app)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()