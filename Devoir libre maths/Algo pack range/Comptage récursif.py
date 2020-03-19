import numpy as np

A = np.array([[0., 1., 0., 0.],
              [0., 0., 0., 1.],
              [1., 1., 0., 0.],
              [1., 0., 1., 0.]])

longueur = len(A)
count = 0
for i in range(longueur):
    for n in range(longueur):      # permet de parcourir la matrice par ses colones
        # print(A[n,i])
        count += A[n, i]
    print("count = ", count)
    A[:, i] = A[:, i]/count
    # print("la pertinence de ce site est de :", 1/count, "(1 fort, 0 faible)")
    count = 0
    print(A)
    A = A.transpose()
    # print(A)
    ValeurPropres, VecteurPropres = np.linalg.eig(A)
    imax = np.argmax(np.abs(ValeurPropres))
    for z in range(ValeurPropres.shape[0]):
        if np.abs(ValeurPropres[z] - 1) < 0.01:
            #print(z)
            V = VecteurPropres[:, z].real
            V = V/np.sum(V)
            print("V", V)
