import numpy as np

A = np.array([[0, 1, 0, 0],
              [0, 0, 0, 1],
              [1, 1, 0, 0],
              [1, 0, 1, 0]])


print("************************ \naddition des colones de la matrice adjacente : \n************************")
comptagenaif1 = 0
for i in A:
    comptagenaif1 += i[0]
print("comptagenaif1 = ", comptagenaif1)

comptagenaif2 = 0
for i in A:
    comptagenaif2 += i[1]
print("comptagenaif2 = ", comptagenaif2)

comptagenaif3 = 0
for i in A:
    comptagenaif3 += i[2]
print("comptagenaif3 = ", comptagenaif3)

comptagenaif4 = 0
for i in A:
    comptagenaif4 += i[3]
print("comptagenaif4 = ", comptagenaif4)


#pour qu'un site soit tres populaire, il doit avoir un comptage naif fort
# => beaucoup de sites doivent renvoyer à lui
