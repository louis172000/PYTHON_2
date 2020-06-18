import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton
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
        self.setMinimumSize(900, 500)
        self.buttons = ButtonsPanel()
        self.affichageverticalprincipal.addWidget(self.buttons)

        #rafraichissement

        self.setLayout(self.affichageverticalprincipal)


class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # 3 boutons du haut
        self.layout = QGridLayout()
        self.button_load_3dmodel = QPushButton("Load 3D model")
        self.button_load_image = QPushButton("Load Image")
        self.button_compute = QPushButton("Compute")
        self.layout.addWidget(self.button_load_3dmodel, 0, 0, 1, 1)
        self.layout.addWidget(self.button_load_image, 0, 1, 1, 1)
        self.layout.addWidget(self.button_compute, 7, 0, 1, 1)

        self.button_compute.clicked.connect(self.graphique_affichage)
        # self.button_load_3dmodel.clicked.connect(self.model3d)

        # créé zone pour la maquette 3D
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        self.axes = plt.axes(projection='3d')
        self.layout.addWidget(self.canvas, 1, 1, 8, 2)

        # boutons de gauche pour séléctionner la maquette à étudier
        self.label1 = QRadioButton("pavé droit")
        self.label2 = QRadioButton("Triangle")
        self.label3 = QRadioButton("cylindre")
        self.label4 = QRadioButton("Mini 6.50")
        self.labelfree = QRadioButton("Renseigner le chemin ci dessous")
        self.textepath = QLineEdit("")
        # self.textepath.resize()
        self.layout.addWidget(self.label1, 1, 0, 1, 1)
        self.layout.addWidget(self.label2, 2, 0, 1, 1)
        self.layout.addWidget(self.label3, 3, 0, 1, 1)
        self.layout.addWidget(self.label4, 4, 0, 1, 1)
        self.layout.addWidget(self.labelfree, 5, 0, 1, 1)
        self.layout.addWidget(self.textepath, 6, 0, 1, 1)

        self.label1.toggled.connect(lambda: self.checkboxes("FichiersSTL\\Rectangular_HULL_Normals_Outward.STL"))   # info du lambda trouvé sur google
        self.label2.toggled.connect(lambda: self.checkboxes("FichiersSTL\\V_HULL_Normals_Outward.STL"))
        self.label3.toggled.connect(lambda: self.checkboxes("FichiersSTL\\Cylindrical_HULL_Normals_Outward.STL"))
        self.label4.toggled.connect(lambda: self.checkboxes("FichiersSTL\\Mini650_HULL_Normals_Outward.STL"))
        self.labelfree.toggled.connect(lambda: self.checkboxes(self.textepath.toPlainText()))


        self.fig_graph = plt.figure()
        self.canvas_graph = FigureCanvas(self.fig_graph)
        self.axes_graph = plt.axes()
        self.axes_graph.plot()                              # fonction à l'intérieur
        # self.canvas_graph.draw()
        self.image_graph = self.canvas_graph
        self.layout.addWidget(self.canvas_graph, 1, 3, 8, 2)

        self.setLayout(self.layout)

    def graphique_affichage(self):
        self.axes.clear()
        self.axes_graph.clear()

        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file(self.path)
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        # Auto scale to the mesh size
        scale = your_mesh.points.flatten('C')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.canvas.draw()


        self.axes_graph.plot([1, 0, 2])
        self.canvas_graph.draw()


        self.setLayout(self.layout)

    def checkboxes(self, fichier):
        self.path = fichier
        # self.axes =
        # print(fichier)
        # self.textepath.text







fichier = 'FichiersSTL\\Mini650_HULL_Normals_Outward.STL'
app = QApplication([])
win = Window()
win.show()
app.exec_()