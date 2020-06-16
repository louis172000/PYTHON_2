import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton
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

        self.grid = QGridLayout()
        self.setMinimumSize(400, 400)


        self.setWindowTitle("IHM")
        self.label_load_3dmodel = QPushButton("Load 3D model")
        self.label_load_image = QPushButton("Load Image")
        self.label_compute = QPushButton("Compute")

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = plt.axes(projection='3d')

        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file('FichiersSTL\\Mini650_HULL.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        # Auto scale to the mesh size
        scale = your_mesh.points.flatten('C')
        self.axes.auto_scale_xyz(scale, scale, scale)

        self.grid.addWidget(self.label_load_3dmodel, 0, 0, 1, 2)
        self.grid.addWidget(self.label_load_image, 0, 2, 1, 2)
        self.grid.addWidget(self.label_compute, 0, 4, 1, 2)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = plt.axes(projection='3d')



        #rafraichissement
        self.canvas.draw()
        self.grid.addWidget(self.canvas, 1, 2, 1, 2)


        self.setLayout(self.grid)






app = QApplication([])
win = Window()
win.show()
app.exec_()