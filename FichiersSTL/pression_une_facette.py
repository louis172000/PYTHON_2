#################################################################################
################  Fonction de la pression sur une facette   #####################
#################################################################################


############## fonction générale ##############

def pointZ0(a,b):
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]
    else:
        return [0,0,0]


############## fonction de la pression sur une facette ##############

def forcePressanteFacette(facette):
    if facette[5]>0 and facette[8]>0 and facette[11]<=0 :
        [facette[3],facette[4],facette[5]] = pointZ0([facette[9],facette[10],facette[11]],[facette[3],facette[4],facette[5]])
        [facette[6],facette[7],facette[8]] = pointZ0([facette[9],facette[10],facette[11]],[facette[6],facette[7],facette[8]])

    elif facette[5]>0 and facette[8]<=0 and facette[11]>0 :
        [facette[3],facette[4],facette[5]] = pointZ0([facette[6],facette[7],facette[8]],[facette[3],facette[4],facette[5]])
        [facette[9],facette[10],facette[11]] = pointZ0([facette[6],facette[7],facette[8]],[facette[9],facette[10],facette[11]])

    elif facette[5]<=0 and facette[8]>0 and facette[11]>0 :
        [facette[9],facette[10],facette[11]] = pointZ0([facette[3],facette[4],facette[5]],[facette[9],facette[10],facette[11]])
        [facette[6],facette[7],facette[8]] = pointZ0([facette[3],facette[4],facette[5]],[facette[6],facette[7],facette[8]])


    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :
        ab = [facette[6]-facette[3],facette[7]-facette[4],facette[8]-facette[5]]
        ac = [facette[9]-facette[3],facette[10]-facette[4],facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceSurNormale = [normeScalaireSurDeux*facette[0],normeScalaireSurDeux*facette[1],normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        rho = 1000
        g = 9.81
        forcePressante = [surfaceSurNormale[0]*rho*g*z,surfaceSurNormale[1]*rho*g*z,surfaceSurNormale[2]*rho*g*z]
        return forcePressante

    else:
        return [0,0,0]
