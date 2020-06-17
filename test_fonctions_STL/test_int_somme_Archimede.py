#########################################################################################
####### Test de la fonction de l'intérieur de la somme de la poussée d'Archimède ########
#########################################################################################


def interieurSommeArchimede(facette):                                                                       #Calcul de l'intérieur de la somme de la formule d'Archimède

    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :                                                 #si la facette est immergée, on calcul la pression de l'eau sur celle-ci
        ab = [facette[6]-facette[3],facette[7]-facette[4],facette[8]-facette[5]]
        ac = [facette[9]-facette[3],facette[10]-facette[4],facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceSurNormale = [normeScalaireSurDeux*facette[0],normeScalaireSurDeux*facette[1],normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        interieurSomme = [surfaceSurNormale[0]*z,surfaceSurNormale[1]*z,surfaceSurNormale[2]*z]
        return interieurSomme

    elif facette[5]>=0 and facette[8]>=0 and facette[11]>=0 :                                                #si la facette n'est pas immergée, on ne calcul pas la pression de l'eau sur celle-ci
        return [0,0,0]



#Nous avons pris une facette de façon arbitraire
objetEtudie = [0,0,1,0,0,-1,1,0,-1,0,1,-1]                             #Après calcul théorique, nous obtenons [0, 0, -0.5]
print(interieurSommeArchimede(objetEtudie))
