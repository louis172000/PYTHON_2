#Calcul de la force de pression sur une facette


def forcePressanteFacette(a,b,c,n):
    ab = [b[0]-a[0],b[1]-a[1],b[2]-a[2]]

    ac = [c[0]-a[0],c[1]-a[1],c[2]-a[2]]

    ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]

    normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2

    surfaceSurNormale = [normeScalaireSurDeux*n[0],normeScalaireSurDeux*n[1],normeScalaireSurDeux*n[2]]

    rho = 1000
    g = 9.81
    forcePressante = [surfaceSurNormale[0]*rho*g,surfaceSurNormale[1]*rho*g,surfaceSurNormale[2]*rho*g]

    return forcePressante

