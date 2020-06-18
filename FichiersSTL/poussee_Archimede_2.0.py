#################################################################################
###################  Fonction de la poussé d'Archimède   ########################
#################################################################################

############### fonctions générales ###############

def pointZ0(a,b):
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]
    else:
        return [0,0,0]


def interieurSommeArchimede(facette):
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
        interieurSomme = [surfaceSurNormale[0]*z,surfaceSurNormale[1]*z,surfaceSurNormale[2]*z]
        return interieurSomme

    elif facette[5]>=0 and facette[8]>=0 and facette[11]>=0 :                                                #si la facette n'est pas immergée, on ne calcul pas la pression de l'eau sur celle-ci
        return [0,0,0]
    else:
        return [0,0,0]

############### fonction de la poussée d'Archimède ###############

def archimede(objet):
    somme = [0,0,0]
    for i in objet:
        if i[5]>=0 and i[8]<0 and i[11]<0 :
            premierNewPoint  = pointZ0([i[3],i[4],i[5]],[i[6],i[7],i[8]])
            deuxiemeNewPoint = pointZ0([i[3],i[4],i[5]],[i[9],i[10],i[11]])
            premierNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],i[9],i[10],i[11]]
            deuxiemeNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2]]
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        elif i[5]<0 and i[8]>=0 and i[11]<0 :
            premierNewPoint  = pointZ0([i[6],i[7],i[8]],[i[3],i[4],i[5]])
            deuxiemeNewPoint = pointZ0([i[6],i[7],i[8]],[i[9],i[10],i[11]])
            premierNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],i[9],i[10],i[11]]
            deuxiemeNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2]]
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        elif i[5]<0 and i[8]<0 and i[11]>=0 :
            premierNewPoint  = pointZ0([i[9],i[10],i[11]],[i[3],i[4],i[5]])
            deuxiemeNewPoint = pointZ0([i[9],i[10],i[11]],[i[6],i[7],i[8]])
            premierNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],i[9],i[10],i[11]]
            deuxiemeNewTriangle = [i[0],i[1],i[2],i[3],i[4],i[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2]]
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        else:
            interieurSomme = interieurSommeArchimede(i)
            somme = [somme[0]+interieurSomme[0], somme[1]+interieurSomme[1], somme[2]+interieurSomme[2]]

    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g, somme[1]*rho*g, somme[2]*rho*g]
    return pousseArchimede

