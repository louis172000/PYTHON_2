import numpy as np

fichier = open("FichiersSTL/Rectangular_HULL.stl")

ligne = fichier.readlines()
del ligne[0]
del ligne[-1]
print(ligne)
nb_triangles = int(len(ligne)/7)
print(nb_triangles)

"""
exemple
solid OBJECT
  facet normal 0 -1 -0
    outer loop
      vertex 0 -1 0
      vertex 2 -1 0
      vertex 2 -1 1
    endloop
  endfacet
  facet normal 0 -1 -0
    outer loop
      vertex 2 -1 0
      vertex 4 -1 0
      vertex 4 -1 1
    endloop
  endfacet
"""

liste_globale = []
liste_triangle = []

for iteration in range(0, nb_triangles-1):
    fin_de_lignenormale = (ligne[0+7*iteration])[15:]
    fin_de_lignenormale = fin_de_lignenormale.split(" ")
    for i in range(0, len(fin_de_lignenormale)):
        fin_de_lignenormale[i] = float(fin_de_lignenormale[i])
        liste_triangle.append(fin_de_lignenormale[i])
    print("fin de ligne Normale", fin_de_lignenormale)

    fin_de_ligneA = (ligne[2+7*iteration])[13:]
    fin_de_ligneA = fin_de_ligneA.split(" ")
    for i in range(0, len(fin_de_ligneA)):
        fin_de_ligneA[i] = float(fin_de_ligneA[i])
        liste_triangle.append(fin_de_ligneA[i])
    print("fin de ligne A      ", fin_de_ligneA)

    fin_de_ligneB = (ligne[3+7*iteration])[13:]
    fin_de_ligneB = fin_de_ligneB.split(" ")
    for i in range(0, len(fin_de_ligneB)):
        fin_de_ligneB[i] = float(fin_de_ligneB[i])
        liste_triangle.append(fin_de_ligneB[i])
    print("fin de ligne B      ", fin_de_ligneB)

    fin_de_ligneC = (ligne[4+7*iteration])[13:]
    fin_de_ligneC = fin_de_ligneC.split(" ")
    for i in range(0, len(fin_de_ligneC)):
        fin_de_ligneC[i] = float(fin_de_ligneC[i])
        liste_triangle.append(fin_de_ligneC[i])
    print("fin de ligne C      ", fin_de_ligneC)
    print("liste du nieme triangle: ", liste_triangle)

    liste_globale.append(liste_triangle)
    # la liste_triangle à été ajoutée
    liste_triangle = []

print("liste globale :", liste_globale)


