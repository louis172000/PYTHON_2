#################################################################################
###################  Fonction de la poussé d'Archimède   ########################
#################################################################################

#Poussée d'Archimède sur un objet en prenant en compte toutes les parties immergées des facettes

############### fonctions générales ###############

def pointZ0(a,b):                                                                   #fonction permettant de trouver le point à z=0 entre un point à z>0 et un point à z<0
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]
    else:
        return [0,0,0]


def interieurSommeArchimede(facette):                                              #Calcul de l'intérieur de la somme de la poussée d'Archimède
    #Nous réduisons les facettes qui ont deux point à z>0, afin d'avoir une leur partie complétement immergée
    if facette[5]>0 and facette[8]>0 and facette[11]<=0 :
        [facette[3],facette[4],facette[5]] = pointZ0([facette[9],facette[10],facette[11]],[facette[3],facette[4],facette[5]])
        [facette[6],facette[7],facette[8]] = pointZ0([facette[9],facette[10],facette[11]],[facette[6],facette[7],facette[8]])

    elif facette[5]>0 and facette[8]<=0 and facette[11]>0 :
        [facette[3],facette[4],facette[5]] = pointZ0([facette[6],facette[7],facette[8]],[facette[3],facette[4],facette[5]])
        [facette[9],facette[10],facette[11]] = pointZ0([facette[6],facette[7],facette[8]],[facette[9],facette[10],facette[11]])

    elif facette[5]<=0 and facette[8]>0 and facette[11]>0 :
        [facette[9],facette[10],facette[11]] = pointZ0([facette[3],facette[4],facette[5]],[facette[9],facette[10],facette[11]])
        [facette[6],facette[7],facette[8]] = pointZ0([facette[3],facette[4],facette[5]],[facette[6],facette[7],facette[8]])


    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :                         #Calcul de l'intérieur de la somme pour la partie immergé d'une facette
        ab = [facette[6]-facette[3],facette[7]-facette[4],facette[8]-facette[5]]
        ac = [facette[9]-facette[3],facette[10]-facette[4],facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceSurNormale = [normeScalaireSurDeux*facette[0],normeScalaireSurDeux*facette[1],normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        interieurSomme = [surfaceSurNormale[0]*z,surfaceSurNormale[1]*z,surfaceSurNormale[2]*z]
        return interieurSomme

    else:                                                                           #si la facette n'est pas du tout immergée, la pression sur celle-ci est négligée
        return [0,0,0]


############### fonction de la poussée d'Archimède ###############

def archimede(objet):                                                               #calcul de la poussée d'Archimède sur un objet composé d'un certain nombre de facette
    somme = [0,0,0]
    for facette2 in objet:
        #Nous étudions tout d'abord les facettes partiellement immergées qui ont un unique point avec un z>=0
        if facette2[5]>=0 and facette2[8]<0 and facette2[11]<0 :                                                                # A positif
            premierNewPoint  = pointZ0([facette2[3],facette2[4],facette2[5]],[facette2[6],facette2[7],facette2[8]])             # Calcul de B'
            deuxiemeNewPoint = pointZ0([facette2[3],facette2[4],facette2[5]],[facette2[9],facette2[10],facette2[11]])           # Calcul de C'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[6],facette2[7],facette2[8],facette2[9],facette2[10],facette2[11]]                               # Triangle B'BC
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],facette2[9],facette2[10],facette2[11]]      # Triangle B'C'C
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        elif facette2[5]<0 and facette2[8]>=0 and facette2[11]<0 :                                                              # B positif
            premierNewPoint  = pointZ0([facette2[6],facette2[7],facette2[8]],[facette2[3],facette2[4],facette2[5]])             # Calcul de A'
            deuxiemeNewPoint = pointZ0([facette2[6],facette2[7],facette2[8]],[facette2[9],facette2[10],facette2[11]])           # Calcul de C'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],facette2[3],facette2[4],facette2[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[9],facette2[10],facette2[11]]                                # Triangle AA'C
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[9],facette2[10],facette2[11]]       # Triangle C'A'C
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        elif facette2[5]<0 and facette2[8]<0 and facette2[11]>=0 :                                                              # C positif
            premierNewPoint  = pointZ0([facette2[9],facette2[10],facette2[11]],[facette2[3],facette2[4],facette2[5]])           # Calcul de A'
            deuxiemeNewPoint = pointZ0([facette2[9],facette2[10],facette2[11]],[facette2[6],facette2[7],facette2[8]])           # Calcul de B'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],facette2[3],facette2[4],facette2[5],facette2[6],facette2[7],facette2[8],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2]]                                  # Triangle ABA'
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],facette2[6],facette2[7],facette2[8],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2]]         # Triangle B'BA'
            interieurSommePremierTriangle = interieurSommeArchimede(premierNewTriangle)
            interieurSommeDeuxiemeTriangle = interieurSommeArchimede(deuxiemeNewTriangle)
            somme = [somme[0]+interieurSommePremierTriangle[0]+interieurSommeDeuxiemeTriangle[0], somme[1]+interieurSommePremierTriangle[1]+interieurSommeDeuxiemeTriangle[1], somme[2]+interieurSommePremierTriangle[2]+interieurSommeDeuxiemeTriangle[2]]

        #Nous étudions ensuite toutes les autres facettes
        else:
            interieurSomme = interieurSommeArchimede(facette2)
            somme = [somme[0]+interieurSomme[0], somme[1]+interieurSomme[1], somme[2]+interieurSomme[2]]

    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g, somme[1]*rho*g, somme[2]*rho*g]
    return pousseArchimede

