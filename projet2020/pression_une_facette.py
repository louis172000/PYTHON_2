#Calcul de la force de pression sur une facette

def forcePressanteFacette(facette):
    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :                                                        #si la facette est imergée, on calcul la pression de l'eau sur celle-ci
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
    elif facette[5]>=0 and facette[8]>=0 and facette[11]>=0 :
        return [0,0,0]
