import numpy as np

def notorieteNaif(A):
    n= A.shape[0]
    p= A.shape[0]
    notoriete = np.zeros((n))
    for j in range(n):
        for i in range(n):
            notoriete[j]+=A[i,j]
    return  notoriete



def notorietePondere(A):
    n= A.shape[0]
    p= A.shape[0]
    nb_liens = np.zeros((n))
    for j in range(n):
        for i in range(n):
            nb_liens[i]+=A[i,j]
    A_pondere=np.zeros(A.shape)
    for j in range(n):
        for i in range(n):
            A_pondere[i,j]=A[i,j]/nb_liens[i]
    notoriete = np.zeros((n))
    for j in range(n):
        for i in range(n):
            notoriete[j]+=A_pondere[i,j]
    return  notoriete

def notorieteRecursif(A):
    n = A.shape[0]                       # donne la taille de la matrice
    p = A.shape[0]
    nb_liens = np.zeros(n)
    for j in range(n):
        for i in range(n):
            nb_liens[i] += A[i, j]
    A_pondere = np.zeros(A.shape)
    for j in range(n):
        for i in range(n):
            A_pondere[i, j] = A[i, j]/nb_liens[i]

    A = A_pondere.transpose()
    (ValeurPropres, VecteurPropres) = np.linalg.eig(A)
    imax = np.argmax(np.abs(ValeurPropres))
    for i in range(ValeurPropres.shape[0]):
        if np.abs(ValeurPropres[i] - 1) < 0.01:
            print(i)
            V=  VecteurPropres[:, i].real
            V=V/np.sum(V)
            return V



A = np.array([[ 0., 1., 0., 0.], [0., 0., 0., 1.], [ 1., 1., 0., 0.], [ 1., 0., 1., 0.]])

print(notorieteNaif(A))
#Pour rendre une site internet populaire, il suffit de créer des sites internets vides qui pointent sur sur ce site

#print(notorietePondere(A))

print(notorieteRecursif(A))
