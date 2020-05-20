from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.label = QLabel("Ceci est un QLabel")
        self.button = QPushButton("Ceci est un QPushButton")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


app = QApplication([])
win = Window()
win.show()
app.exec_()