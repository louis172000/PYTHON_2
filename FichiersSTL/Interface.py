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
        self.Buttons = ButtonsPanel()
        self.affichageverticalprincipal.addWidget(self.Buttons)


        #rafraichissement
        # self.canvas.draw()

        self.setLayout(self.affichageverticalprincipal)



class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.Hlayout = QHBoxLayout()

        self.label_load_3dmodel = QPushButton("Load 3D model")
        self.label_load_image = QPushButton("Load Image")
        self.button_compute = QPushButton("Compute")

        self.Hlayout.addWidget(self.label_load_3dmodel)
        self.Hlayout.addWidget(self.label_load_image)
        self.Hlayout.addWidget(self.button_compute)

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = plt.axes(projection='3d')
        self.Hlayout.addWidget(self.canvas)
        # self.Horlayout = QHBoxLayout()


        # self.label_load_3dmodel.clicked.connect(self.liste_models)
        # self.label_compute.clicked.connect(self.graphique_affichage)

        self.button_compute.clicked.connect(self.graphique_affichage)
        self.setLayout(self.Hlayout)

    def liste_models(self):
        self.grid.repaint()

    def graphique_affichage(self):
        print(1)

        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file('STL_Normals_Outward\\Mini650_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        # Auto scale to the mesh size
        scale = your_mesh.points.flatten('C')
        self.axes.auto_scale_xyz(scale, scale, scale)

        # self.Hlayout.addWidget(self.canvas)
        # self.Widget(self.Horlayout)
        # self.addWidget(self.canvas)



app = QApplication([])
win = Window()
win.show()
app.exec_()