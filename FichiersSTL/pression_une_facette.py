#Calcul de la force de pression sur une facette


def surfaceFacetteNormee(a,b,c,n):
    ab = [b[0]-a[0],b[1]-a[1],b[2]-a[2]]

    ac = [c[0]-a[0],c[1]-a[1],c[2]-a[2]]

    scalaire = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]

    normeScalaireSurDeux = (((scalaire[0]**2)+(scalaire[1]**2)+(scalaire[2]**2))**(1/2))/2

    surfaceParNormale = [normeScalaireSurDeux*n[0],normeScalaireSurDeux*n[1],normeScalaireSurDeux*n[2]]

    return surfaceParNormale

def forcePressanteFacette(a,b,c,n):
    rho = 1000
    g = 9.81
    surface = surfaceFacetteNormee(a,b,c,n)
    forcePressante = [surface[0]*rho*g,surface[1]*rho*g,surface[2]*rho*g]

    return forcePressante

#test Programme
a = [2,1,2]
b = [3,4,1]
c = [2,4,3]
n = [0,-1,1]

print(surfaceFacetteNormee(a,b,c,n))
print(forcePressanteFacette(a,b,c,n))
