import numpy as np
import random

A = np.array([[0., 1., 0., 0.],
              [0., 0., 0., 1.],
              [1., 1., 0., 0.],
              [1., 0., 1., 0.]])

N = random.random()
N = int(N*100000)
print(N)


def comptageRecursif(A):
    n = A.shape[0]
    nb_liens = np.zeros((n))
    for j in range(n):
        for i in range(n):
            nb_liens[i] += A[i, j]
    A_pondere = np.zeros(A.shape)
    for j in range(n):
        for i in range(n):
            A_pondere[i,j] = A[i, j]/nb_liens[i]
    print('A', A_pondere)
    A = A_pondere.transpose()
    # print(A)
    ValeurPropres, VecteurPropres = np.linalg.eig(A)
    imax = np.argmax(np.abs(ValeurPropres))
    for i in range(ValeurPropres.shape[0]):
        if np.abs(ValeurPropres[i] - 1) < 0.01:
            #print(i)
            V = VecteurPropres[:, i].real
            V = V/np.sum(V)
            return V



###
A = np.array([[ 0, 1, 0, 0], [0, 0, 0, 1], [ 1, 1, 0, 0], [ 1, 0, 1, 0]])
#print(A)
# print(comptageNaif(A))
#Pour rendre une site internet populaire, il suffit de créer des sites internets vides qui pointent sur sur ce site

# print(comptagePondere(A))

print(comptageRecursif(A))
