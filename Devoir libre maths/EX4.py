import random
import numpy.random as rd


def permute(n):
    permutation = []
    for i in range(0, n):
        #print(i)
        permutation.append(i)
        #print(x)
    random.shuffle(permutation)
    #print(permutation)
    return permutation


def pointFixe(permutation, n):
    #print(permutation)
    for i in range(0, n):
        if permutation[i] == i:
            return True
    return False


def probaCorrection(n, nbexp):
    saCopie = 0
    for i in range(0, nbexp):
        permutation = permute(n)
        #print(pointFixe(permutation,n))
        if pointFixe(permutation, n):
            saCopie += 1
    esperance = saCopie/nbexp
    return esperance


n = 29
nbexp = 10000

print(probaCorrection(n, nbexp))
