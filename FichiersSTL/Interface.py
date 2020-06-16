from PySide2.QtWidgets import *
# QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QGridLayout, QTextEdit, text

"""

utilisation de grid :
(self.XXX, ligne, colone, position hauteur, largeur)

"""

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.grid = QGridLayout()
        self.setMinimumSize(400, 400)


        self.setWindowTitle("IHM")
        self.labelload_3dmodel = QPushButton("Load 3D model")
        self.labelload_image = QPushButton("Load Image")
        self.label_compute = QPushButton("Compute")


        self.grid.addWidget(self.labelload_3dmodel, 0, 0, 1, 2)
        self.grid.addWidget(self.labelload_image, 0, 2, 1, 2)
        self.grid.addWidget(self.label_compute, 0, 4, 1, 2)



        self.setLayout(self.grid)





app = QApplication([])
win = Window()
win.show()
app.exec_()