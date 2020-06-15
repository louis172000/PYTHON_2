fichier = open("FichiersSTL/Rectangular_HULL.stl")
#print(fichier.read())

ligne = fichier.readlines()
print(ligne)

i=3
j=4
k=5



coor1 = ligne[3].split()
del coor1[0]
print(coor1)
coor2 = ligne[4].split()
del coor2[0]
print(coor2)
coor3 = ligne[5].split()
del coor3[0]
print(coor3)






