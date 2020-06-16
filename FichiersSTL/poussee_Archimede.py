import numpy as np

sommeForcePression = 0

matrice = np.array([
    [1,2,3,     6,5,4,     7,8,9,     12,11,10],
    [13,14,15,  18,17,16,  19,20,21,  24,23,22],
    [25,26,27,  30,29,28,  31,32,33,  36,35,34],
])


def pousseeTotale(ligneMatrice):
    ab = [ligneMatrice[6]-ligneMatrice[3],ligneMatrice[7]-ligneMatrice[4],ligneMatrice[8]-ligneMatrice[5]]
    ac = [ligneMatrice[9]-ligneMatrice[3],ligneMatrice[10]-ligneMatrice[4],ligneMatrice[11]-ligneMatrice[5]]
    ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
    normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
    surfaceSurNormale = [normeScalaireSurDeux*ligneMatrice[0],normeScalaireSurDeux*ligneMatrice[1],normeScalaireSurDeux*ligneMatrice[2]]
    z = (ligneMatrice[5]+ligneMatrice[8]+ligneMatrice[11])/3
    pousseeTot = [surfaceSurNormale[0]*z*9810,surfaceSurNormale[1]*z*9810,surfaceSurNormale[2]*z*9810]

    return pousseeTot

def archimede(matrice):
    somme = [0,0,0]
    for i in matrice:
        somme = [somme[0]+pousseeTotale(i)[0],somme[1]+pousseeTotale(i)[1],somme[2]+pousseeTotale(i)[2]]

    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g,somme[1]*rho*g,somme[2]*rho*g]

    return pousseArchimede

print(archimede(matrice))
