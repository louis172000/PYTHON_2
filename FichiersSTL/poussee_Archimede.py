#################################################################################
###################  Fonction de la poussé d'Archimède   ########################
#################################################################################

#Poussée d'Archimède sur un objet en prenant en compte seulement les facettes complétement immergées

def interieurSommeArchimede(facette):                                                                    #Calcul de l'intérieur de la somme de la poussée d'Archimède
    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :                                              #si la facette est entièrement immergée, on calcul la pression de l'eau sur celle-ci
        ab = [facette[6]-facette[3],facette[7]-facette[4],facette[8]-facette[5]]
        ac = [facette[9]-facette[3],facette[10]-facette[4],facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceParNormale = [normeScalaireSurDeux*facette[0],normeScalaireSurDeux*facette[1],normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        interieurSomme = [surfaceParNormale[0]*z,surfaceParNormale[1]*z,surfaceParNormale[2]*z]
        return interieurSomme

    else :                                                                                               #si la facette n'est pas complétement immergée, la pression sur celle-ci est négligée
        return [0,0,0]


def archimede(objet):                                                                                    #calcul de la poussée d'Archimède sur un objet composé d'un certain nombre de facette
    somme = [0,0,0]
    for i in objet:                                                                                      #Calcul de la somme de la poussée d'Archimède
        interieurSomme = interieurSommeArchimede(i)
        somme = [somme[0]+interieurSomme[0],somme[1]+interieurSomme[1],somme[2]+interieurSomme[2]]
    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g,somme[1]*rho*g,somme[2]*rho*g]

    return pousseArchimede
