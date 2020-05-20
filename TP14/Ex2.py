from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QGridLayout, QTextEdit

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.grid = QGridLayout()

        self.setWindowTitle("IHM")
        self.labelcmt = QLabel("Laissez un commentaire")
        self.labeltxt = QTextEdit()
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")
        """
        
        utilisation de grid :
        (self.XXX, ligne, colone, hauteur, largeur)
        
        """
        self.grid.addWidget(self.labelcmt, 0, 0, 1, 2)
        self.grid.addWidget(self.labeltxt, 1, 0, 1, 2)

        self.grid.addWidget(self.button1, 2, 0, 1, 1)
        self.grid.addWidget(self.button2, 2, 1, 1, 1)

        self.setLayout(self.grid)






app = QApplication([])
win = Window()
win.show()
app.exec_()