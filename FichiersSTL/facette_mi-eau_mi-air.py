############### Fonctions générales ###############

def pointZ0(a,b):
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]


def newTriangle(facette):
    if facette[5]>=0 and facette[8]>=0 and facette[11]<=0 :                                                     #dernier point avec z < 0
        [facette[3],facette[4],facette[5]] = pointZ0([facette[9],facette[10],facette[11]],[facette[3],facette[4],facette[5]])               #facettes a z>0 qu'on remplace
        [facette[6],facette[7],facette[8]] = pointZ0([facette[9],facette[10],facette[11]],[facette[6],facette[7],facette[8]])               #

    elif facette[5]>=0 and facette[8]<=0 and facette[11]>=0 :                                                   #deuxieme point avec z < 0
        [facette[3],facette[4],facette[5]] = pointZ0([facette[6],facette[7],facette[8]],[facette[3],facette[4],facette[5]])                 #facettes a z>0 qu'on remplace
        [facette[9],facette[10],facette[11]] = pointZ0([facette[6],facette[7],facette[8]],[facette[9],facette[10],facette[11]])             #

    elif facette[5]<=0 and facette[8]>=0 and facette[11]>=0 :                                                   #premier point avec z < 0
        [facette[9],facette[10],facette[11]] = pointZ0([facette[3],facette[4],facette[5]],[facette[9],facette[10],facette[11]])             #facettes a z>0 qu'on remplace
        [facette[6],facette[7],facette[8]] = pointZ0([facette[3],facette[4],facette[5]],[facette[6],facette[7],facette[8]])                 #

    return facette





def deuxNewtriangle(facette2):
    if facette2[5]>=0 and facette2[8]<0 and facette2[11]<0 :                                                             # A positif
            premierNewPoint  = pointZ0([facette2[3],facette2[4],facette2[5]],[facette2[6],facette2[7],facette2[8]])      # Calcul de B'
            deuxiemeNewPoint = pointZ0([facette2[3],facette2[4],facette2[5]],[facette2[9],facette2[10],facette2[11]])    # Calcul de C'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[6],facette2[7],facette2[8],facette2[9],facette2[10],facette2[11]]                               # Triangle B'BC
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],facette2[9],facette2[10],facette2[11]]      # Triangle B'C'C

            return premierNewTriangle,deuxiemeNewTriangle

    elif facette2[5]<0 and facette2[8]>=0 and facette2[11]<0 :                                                           # B positif
            premierNewPoint  = pointZ0([facette2[6],facette2[7],facette2[8]],[facette2[3],facette2[4],facette2[5]])      # Calcul de A'
            deuxiemeNewPoint = pointZ0([facette2[6],facette2[7],facette2[8]],[facette2[9],facette2[10],facette2[11]])    # Calcul de C'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],facette2[3],facette2[4],facette2[5],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[9],facette2[10],facette2[11]]                                # Triangle AA'C
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2],facette2[9],facette2[10],facette2[11]]       # Triangle C'A'C

            return premierNewTriangle,deuxiemeNewTriangle

    elif facette2[5]<0 and facette2[8]<0 and facette2[11]>=0 :                                                           # C positif
            premierNewPoint  = pointZ0([facette2[9],facette2[10],facette2[11]],[facette2[3],facette2[4],facette2[5]])    # Calcul de A'
            deuxiemeNewPoint = pointZ0([facette2[9],facette2[10],facette2[11]],[facette2[6],facette2[7],facette2[8]])    # Calcul de B'
            premierNewTriangle = [facette2[0],facette2[1],facette2[2],facette2[3],facette2[4],facette2[5],facette2[6],facette2[7],facette2[8],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2]]                                  # Triangle ABA'
            deuxiemeNewTriangle = [facette2[0],facette2[1],facette2[2],deuxiemeNewPoint[0],deuxiemeNewPoint[1],deuxiemeNewPoint[2],facette2[6],facette2[7],facette2[8],premierNewPoint[0],premierNewPoint[1],premierNewPoint[2]]         # Triangle B'BA'

            return premierNewTriangle,deuxiemeNewTriangle



##########################################################
#################    Main program    #####################
##########################################################

#                      A         B          C
                   #########  ########  #########
facette = [0,0,0,  0,-1,-0.5,  0,0,0.5,  0,0,0.5]

print("Nouveau triangle :",newTriangle(facette))
print()



#                      A         B          C
                   #########  ########  #########
facette2 = [0,0,0,  4,0,-0.5,  4,1,-0.5,  4,1,0.5]
print("deux nouveau triangle :",deuxNewtriangle(facette2))
