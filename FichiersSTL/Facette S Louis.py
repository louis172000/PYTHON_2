import numpy as np
fichier = open("FichiersSTL/Cylindrical_HULL.stl")

############################################################################
#############             Definitions de fonctions             #############
############################################################################


def fonction_coordonnees_globales(liste, liste_triangle):
    liste = liste.split(" ")
    for i in range(0, len(liste)):
        liste[i] = float(liste[i])
        liste_triangle.append(liste[i])                 # ajoute les coordonnées (du type float) à la liste du triangle en question
    # print("liste :", liste)


def creation_liste_globale(ligne):
    liste_globale = []
    liste_triangle = []
    for iteration in range(0, nb_triangles):
        fin_de_lignenormale = (ligne[0+7*iteration])[15:]                   # récupere les derniers éléments de la ligne
        fonction_coordonnees_globales(fin_de_lignenormale, liste_triangle)

        fin_de_ligne_a = (ligne[2+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_a, liste_triangle)

        fin_de_ligne_b = (ligne[3+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_b, liste_triangle)

        fin_de_ligne_c = (ligne[4+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_c, liste_triangle)

        # print("liste du nieme triangle: ", liste_triangle)

        liste_globale.append(liste_triangle)
        # la liste_triangle à été ajoutée
        liste_triangle = []

    return liste_globale

############################################################################
#############                   Main program                   #############
############################################################################


ligne = fichier.readlines()     # chaque élément représente une ligne
del ligne[0]
del ligne[-1]                   # supprime le premier et dernier élément extrait du fichier STL
# print(ligne)
nb_triangles = int(len(ligne)/7)
print("Structure composée de :", nb_triangles, "triangles")
print("""clasée de la façon suivante: liste_globale = [coordonées du triangle1 (type:liste), coordonées du triangle2 (type:liste), ...]
""")

liste_globale = creation_liste_globale(ligne)
# print("liste globale :", liste_globale)

