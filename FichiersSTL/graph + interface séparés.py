import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton
from PySide2.QtWidgets import *
from stl import mesh
from mpl_toolkits import mplot3d
import numpy as np
import time


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Projet 2020 Navire")

        self.affichageverticalprincipal = QVBoxLayout()
        self.setMinimumSize(800, 400)
        self.buttons = Affichage()
        self.affichageverticalprincipal.addWidget(self.buttons)

        # rafraichissement
        self.setLayout(self.affichageverticalprincipal)


class Affichage(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # 3 boutons du haut
        self.layout = QGridLayout()
        self.button_load_3dmodel = QLabel("Load 3D model")
        self.button_compute = QPushButton("Calculer")
        self.layout.addWidget(self.button_load_3dmodel, 0, 0, 1, 0)
        self.layout.addWidget(self.button_compute, 10, 0, 1, 1)
        self.button_compute.hide()

        self.button_compute.clicked.connect(self.graphique_affichage)

        # créé zone pour la maquette 3D
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        self.axes = plt.axes(projection='3d')
        self.layout.addWidget(self.canvas, 0, 1, 12, 2)

        # boutons de gauche pour séléctionner la maquette à étudier
        self.label_preenregistre = QLabel("Pré-enregistré :")
        self.label1 = QRadioButton("pavé droit")
        self.label2 = QRadioButton("Triangle")
        self.label3 = QRadioButton("cylindre")
        self.label4 = QRadioButton("Mini 6.50")
        self.label_add_another = QLabel("En ajouter un autre :")
        self.labelfree = QRadioButton("Autre")
        self.textepath = QLineEdit("")
        # collez le chemin ci dessous
        self.label_path_non_valide = QLabel("Chemin non valide")
        self.validation = QRadioButton("Valider")

        self.layout.addWidget(self.label_preenregistre, 1, 0, 1, 1)
        self.layout.addWidget(self.label1, 2, 0, 1, 1)
        self.layout.addWidget(self.label2, 3, 0, 1, 1)
        self.layout.addWidget(self.label3, 4, 0, 1, 1)
        self.layout.addWidget(self.label4, 5, 0, 1, 1)
        self.layout.addWidget(self.label_add_another,6, 0, 1, 1)
        self.layout.addWidget(self.labelfree, 7, 0, 1, 1)
        self.layout.addWidget(self.textepath, 8, 0, 1, 1)
        self.layout.addWidget(self.validation, 9, 0, 1, 1)
        self.layout.addWidget(self.label_path_non_valide, 10, 0, 1, 1)
        self.textepath.hide()
        self.validation.hide()
        self.label_path_non_valide.hide()

        self.label1.toggled.connect(lambda: self.checkboxes(
            "FichiersSTL\\Rectangular_HULL_Normals_Outward.STL"))  # utilisation du lambda trouvé sur google
        self.label2.toggled.connect(lambda: self.checkboxes("FichiersSTL\\V_HULL_Normals_Outward.STL"))
        self.label3.toggled.connect(lambda: self.checkboxes("FichiersSTL\\Cylindrical_HULL_Normals_Outward.STL"))
        self.label4.toggled.connect(lambda: self.checkboxes("FichiersSTL\\Mini650_HULL_Normals_Outward.STL"))
        self.labelfree.toggled.connect(lambda: self.checkboxes_other())
        self.validation.toggled.connect(lambda: self.checkedBoxes_valided(self.textepath.text()))

        # STL_Nouveaux\\BargeAlu_L_2980_W_633_H_400_NormalOutward2.STL
        # STL_Nouveaux\\WIGLEY_L=2500_B=250_T=156_NormalOutward2.STL
        self.fig_graph = plt.figure()
        self.canvas_graph = FigureCanvas(self.fig_graph)
        self.axes_graph = plt.axes()
        self.axes_graph.plot()  # fonction à l'intérieur
        self.image_graph = self.canvas_graph
        self.layout.addWidget(self.canvas_graph, 0, 3, 12, 2)

        self.affichage_force = QLabel("La position finale est de : ")
        self.layout.addWidget(self.affichage_force, 11, 0, 1, 1)
        self.setLayout(self.layout)

    def graphique_affichage(self):

        self.axes.clear()


        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file(self.path)
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        # Auto scale to the mesh size
        scale = your_mesh.points.flatten('C')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.canvas.draw()

        self.axes_graph.clear()
        self.axes_graph.grid()
        self.axes_graph.plot(calculs.x, calculs.y, "red")
        self.canvas_graph.draw()
        texte = "Le tirant d'eau est de : " + str((int(abs(calculs.y[-1])*1000))/1000) + "m"
        self.affichage_force.setText(texte)
        self.button_compute.hide()
        self.textepath.hide()
        self.validation.hide()
        self.textepath.clear()
        self.setLayout(self.layout)

    def checkboxes(self, fichier):
        self.path = fichier
        self.textepath.hide()
        self.validation.hide()
        self.fichierouvert = open(self.path)
        calculs.executer_listeSTL(self)
        self.label_path_non_valide.hide()
        self.button_compute.show()

    def checkboxes_other(self):
        self.textepath.show()
        self.setLayout((self.layout))
        print(self.textepath.text())

        self.validation.show()
        self.label_path_non_valide.hide()
        self.button_compute.hide()

    def checkedBoxes_valided(self, fichier):
        if self.textepath.text() == None or self.textepath.text() == "collez le chemin ici" or self.textepath.text()[-4:] != ".STL":
            # print(self.textepath.text())
            self.labelfree.setChecked(True)
            self.label_path_non_valide.show()
            return
        self.path = fichier
        print(self.path)

        self.fichierouvert = open(self.path)
        calculs.executer_listeSTL(self)
        self.label_path_non_valide.hide()
        self.button_compute.show()


# ################## début de la partie calcul ################### #

class calculs(Affichage):
    def fonction_coordonnees_globales(self, liste, liste_triangle):
        liste = liste.split(" ")
        for i in range(0, len(liste)):
            liste[i] = float(liste[i])
            liste_triangle.append(
                liste[i])  # ajoute les coordonnées (du type float) à la liste du triangle en question
            # print("liste :", liste)

    def listeSTL(self):
        # ouverture fichier + insertion des lignes dans une liste : nb_triangle
        ligne = self.fichierouvert.readlines()
        # supprime le premier et dernier élément extrait du fichier STL
        del ligne[0]
        del ligne[-1]
        self.nb_triangles = int(len(ligne) / 7)
        liste_globale = []
        liste_triangle = []
        # print("Structure composée de :", self.nb_triangles, "triangles")
        # print("""Classée de la façon suivante:
        # liste_globale = [coordonées du triangle1 (type:liste), coordonées du triangle2 (type:liste), ...]
        # """)

        # récupération des coordonnées d'un triangle + sa normale et l'inclue dans la liste globale
        for iteration in range(0, self.nb_triangles):
            self.fin_de_lignenormale = (ligne[0 + 7 * iteration])[15:]  # récupère les derniers éléments de la ligne
            calculs.fonction_coordonnees_globales(self, self.fin_de_lignenormale, liste_triangle)
            self.fin_de_ligne_a = (ligne[2 + 7 * iteration])[13:]
            calculs.fonction_coordonnees_globales(self, self.fin_de_ligne_a, liste_triangle)
            self.fin_de_ligne_b = (ligne[3 + 7 * iteration])[13:]
            calculs.fonction_coordonnees_globales(self, self.fin_de_ligne_b, liste_triangle)
            self.fin_de_ligne_c = (ligne[4 + 7 * iteration])[13:]
            calculs.fonction_coordonnees_globales(self, self.fin_de_ligne_c, liste_triangle)
            liste_globale.append(liste_triangle)
            # la liste_triangle à été ajoutée à liste_globale
            # on vide la liste triangle pour la calcul du triangle suivant
            liste_triangle = []
        return liste_globale

    def interieurSommeArchimede(self, facette):
        if facette[5] >= 0 and facette[8] >= 0 and facette[11] >= 0:
            ab = [facette[6] - facette[3], facette[7] - facette[4], facette[8] - facette[5]]
            ac = [facette[9] - facette[3], facette[10] - facette[4], facette[11] - facette[5]]
            ab_scalaire_ac = [ab[1] * ac[2] - ab[2] * ac[1], ab[2] * ac[0] - ab[0] * ac[2],
                              ab[0] * ac[1] - ab[1] * ac[0]]
            normeScalaireSurDeux = (((ab_scalaire_ac[0] ** 2) + (ab_scalaire_ac[1] ** 2) + (
                    ab_scalaire_ac[2] ** 2)) ** (1 / 2)) / 2
            surfaceParNormale = [normeScalaireSurDeux * facette[0], normeScalaireSurDeux * facette[1],
                                 normeScalaireSurDeux * facette[2]]
            z = (facette[5] + facette[8] + facette[11]) / 3
            interieurSomme = [surfaceParNormale[0] * z, surfaceParNormale[1] * z, surfaceParNormale[2] * z]
            return interieurSomme

        elif facette[5] <= 0 and facette[8] <= 0 and facette[11] <= 0:
            return [0, 0, 0]
        else:
            return [0, 0, 0]

    def archimede(self, objet):
        somme = [0, 0, 0]
        for i in objet:
            interieurSomme = calculs.interieurSommeArchimede(self, i)
            somme = [somme[0] + interieurSomme[0], somme[1] + interieurSomme[1], somme[2] + interieurSomme[2]]
        rho = 1000
        g = 9.81
        pousseArchimede = [somme[0] * rho * g, somme[1] * rho * g, somme[2] * rho * g]
        return pousseArchimede

    def Translate(self, translation, STL):
        for i in range(0, len(STL)):
            STL[i][5] = translation
            STL[i][8] = translation
            STL[i][11] = translation
        return STL

        # Fonction dichotomie

    def dichotomie(self, Zga, Zgb, eps, masse, STL):
        Archimede = calculs.archimede(self, STL)
        # Détermination du Poids en fonction de la masse et de g
        g = 9.81
        Poids = [0, 0, -masse * g]
        # Image des bornes de l'intervalle
        fZga = calculs.f(self, Zga, Archimede, Poids)
        # Compteur d'itérations
        n = 0
        # Création d'une liste des itérations qui serviront d'abscisses pour le graphique
        listeIteration = []
        # Création d'une liste des coordonnées qui serviront d'ordonnées pour le graphique
        listeCoordonneesZ = []
        # On prend le milieu de l'intervalle à chaque tour de boucle, et on élimine la partie qui ne contient pas ce que l'on recherche
        while Zgb - Zga > eps:
            Zgm = (Zgb + Zga) / 2
            fZgm = calculs.f(self, Zgm, Archimede, Poids)
            if fZga * fZgm < 0:
                Zgb = Zgm
                # print(Zgm)
            else:
                Zga = Zgm
                fZga = fZgm
            # print(Translate(Zgm,STL))
            # Ajout de l'itération à chaque tour de boucle
            listeIteration.append(n)
            # Ajout de Zgm à chaque tour de boucle
            listeCoordonneesZ.append(Zgm)
            n += 1
        # print("Nombre d'itérations = ", n)
        del listeIteration[0]
        del listeCoordonneesZ[0]
        return Zga, listeIteration, listeCoordonneesZ

    # Fonction pour trouver Zg, la position d'équilibre
    def f(self, x, Archimede, Poids):
        return Archimede[2] * x - Poids[2]

    def executer_listeSTL(self):
        objetEtudier = calculs.listeSTL(self)

        # print("Tirant d'eau =",dichotomie(f,-40,40,0.001,4000,objetEtudier)[0],"m")
        # print("Liste itérations :",dichotomie(f,-40,40,0.001,4000,objetEtudier)[1],"m")
        # print("Liste coordonnées de z :",dichotomie(f,-40,40,0.001,4000,objetEtudier)[2],"m")

        calculs.x = np.array(calculs.dichotomie(self, -40, 40, 0.001, 4000, objetEtudier)[1])
        calculs.y = np.array(calculs.dichotomie(self, -40, 40, 0.001, 4000, objetEtudier)[2])
    # plt.plot(x, y)
    # plt.show()


app = QApplication([])
win = Window()
win.show()
app.exec_()