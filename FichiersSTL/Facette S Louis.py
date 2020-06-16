import numpy as np

fichier = open("FichiersSTL/Rectangular_HULL.stl")
#print(fichier.read())

ligne = fichier.readline()
list_ligne = ligne.split(" ")
print(len(list_ligne))
list_ligne = [0, 0, 0, 0]

# Matrice_triangle = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

i=3
j=4
k=5
Matrice_triangle = np.array([])

def coordonnées(ligne, list_ligne, Matrice_triangle):
    while len(list_ligne) >= 4:
        ligne = fichier.readline()
        for i in ligne:
            list_ligne = ligne.split(" ")
        print(list_ligne)
        if list_ligne[2] == "facet":
            print(1)
            matrice_blanche = np.zeros(14)
            Matrice_triangle = np.l_[Matrice_triangle, matrice_blanche]
            print(Matrice_triangle)
            co1 = list_ligne[4]
            co2 = list_ligne[5]
            co3 = list_ligne[6]
            Matrice_triangle[0][0] = co1
            Matrice_triangle[0][1] = co2
            Matrice_triangle[0][2] = co3
            print("M = ", Matrice_triangle)






coordonnées(ligne, list_ligne, Matrice_triangle)


