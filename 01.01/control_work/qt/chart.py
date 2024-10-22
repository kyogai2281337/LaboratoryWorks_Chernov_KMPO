from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Круговая диаграмма')
        self.setFixedSize(QSize(800, 600))
        self.createMenu()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

    def createMenu(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        fileMenu = QMenu('Файл', self)
        menubar.addMenu(fileMenu)

        saveAction = QAction('Сохранить', self)
        saveAction.triggered.connect(self.saveChart)
        fileMenu.addAction(saveAction)

        openAction = QAction('Открыть', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        editMenu = QMenu('Редактирование', self)
        menubar.addMenu(editMenu)

        undoAction = QAction('Отменить', self)
        undoAction.triggered.connect(self.undo)
        editMenu.addAction(undoAction)

        redoAction = QAction('Вперед', self)
        redoAction.triggered.connect(self.redo)
        editMenu.addAction(redoAction)

        aboutMenu = QMenu('О Приложении', self)
        menubar.addMenu(aboutMenu)

        aboutAction = QAction('О Приложении', self)
        aboutAction.triggered.connect(self.about)
        aboutMenu.addAction(aboutAction)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '.', 'Текстовые файлы (*.txt)')
        if filename:
            self.loadChartData(filename)

    def loadChartData(self, filename):
        with open(filename, 'r') as f:
            data = [line.strip() for line in f.readlines()]
        self.createPieChart(data)

    def createPieChart(self, data):
        labels = [line.split(':')[0] for line in data]
        sizes = [float(line.split(':')[1].replace(' трлн рублей', '')) for line in data]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        self.canvas.draw()

    def saveChart(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '.', 'Изображения (*.png)')
        if filename:
            self.figure.savefig(filename)

    def undo(self):
        pass

    def redo(self):
        pass

    def about(self):
        QMessageBox.about(self, 'О Приложении', 'Круговая диаграмма')

if __name__ == '__main__':
    app = QApplication([])
    window = ChartWindow()
    window.show()
    app.exec()