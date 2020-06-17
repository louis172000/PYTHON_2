import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton
from PySide2.QtWidgets import *
from stl import mesh
from mpl_toolkits import mplot3d



# QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QGridLayout, QTextEdit, text

"""

utilisation de grid :
(self.XXX, ligne, colone, position hauteur, largeur)
"""

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")

        self.affichageverticalprincipal = QVBoxLayout()
        self.setMinimumSize(400, 400)
        self.buttons = ButtonsPanel()
        self.affichageverticalprincipal.addWidget(self.buttons)

        self.graphiques = H2layout()
        self.affichageverticalprincipal.addWidget(self.graphiques)

        #rafraichissement
        # self.canvas.draw()

        self.setLayout(self.affichageverticalprincipal)



class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.H1Layout = QHBoxLayout()
        self.button_load_3dmodel = QPushButton("Load 3D model")
        self.button_load_image = QPushButton("Load Image")
        self.button_compute = QPushButton("Compute")
        self.H1Layout.addWidget(self.button_load_3dmodel)
        self.H1Layout.addWidget(self.button_load_image)
        self.H1Layout.addWidget(self.button_compute)

        H2 = H2layout()

        self.button_compute.clicked.connect(H2.graphique_affichage)
        self.setLayout(self.H1Layout)


class H2layout(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.H2layout = QHBoxLayout()
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = plt.axes(projection='3d')
        self.H2layout.addWidget(self.canvas)

        self.setLayout(self.H2layout)
        # self.graphique_affichage()

    def graphique_affichage(self):

        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file('FichiersSTL\\Mini650_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        # Auto scale to the mesh size
        scale = your_mesh.points.flatten('C')
        self.axes.auto_scale_xyz(scale, scale, scale)

        self.setLayout(self.H2layout)


app = QApplication([])
win = Window()
win.show()
app.exec_()