import numpy as np

A = np.array([[0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 0.0, 1.0],
              [1.0, 1.0, 0.0, 0.0],
              [1.0, 0.0, 1.0, 0.0]])
n = 0
count = float(0)
compteur = 0
for i in A:
    for n in i:
        count += float(n)
    # print("count = ", count)
    i = i/count
    print("la pertinence de ce site est de :", 1/count, "(1 fort, 0 faible)")
    count = 0
    print(i)


# pour que notre page soit populaire, il faut etre sité par des sites qui n'ont
# pas l'habitude de citer beaucoup de sites
