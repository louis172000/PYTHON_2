def pointZ0(a,b):
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]

#                      A         B          C
                   #########  ########  #########
facette = [0,0,0,  0,-1,-0.5,  0,0,0.5,  0,0,0.5]

if facette[5]>=0 and facette[8]>=0 and facette[11]<=0 :                                                     #dernier point avec z < 0
    [facette[3],facette[4],facette[5]] = pointZ0([facette[9],facette[10],facette[11]],[facette[3],facette[4],facette[5]])               #facettes a z>0 qu'on remplace
    [facette[6],facette[7],facette[8]] = pointZ0([facette[9],facette[10],facette[11]],[facette[6],facette[7],facette[8]])               #

elif facette[5]>=0 and facette[8]<=0 and facette[11]>=0 :                                                   #deuxieme point avec z < 0
    [facette[3],facette[4],facette[5]] = pointZ0([facette[6],facette[7],facette[8]],[facette[3],facette[4],facette[5]])                 #facettes a z>0 qu'on remplace
    [facette[9],facette[10],facette[11]] = pointZ0([facette[6],facette[7],facette[8]],[facette[9],facette[10],facette[11]])             #

elif facette[5]<=0 and facette[8]>=0 and facette[11]>=0 :                                                   #premier point avec z < 0
    [facette[9],facette[10],facette[11]] = pointZ0([facette[3],facette[4],facette[5]],[facette[9],facette[10],facette[11]])             #facettes a z>0 qu'on remplace
    [facette[6],facette[7],facette[8]] = pointZ0([facette[3],facette[4],facette[5]],[facette[6],facette[7],facette[8]])                 #

print("deux point positif",facette)


#                      A         B          C
                   #########  ########  #########
facette = [0,0,0,  4,0,-0.5,  4,1,-0.5,  4,1,0.5]

if facette[5]>=0 and facette[8]<=0 and facette[11]<=0 :                                                      #seul le premier point a son z>0
    memoirePointPositif = [facette[3],facette[4],facette[5]]
    premierNewPoint  = pointZ0([facette[3],facette[4],facette[5]],[facette[6],facette[7],facette[8]])
    deuxiemeNewPoint = pointZ0([facette[3],facette[4],facette[5]],[facette[9],facette[10],facette[11]])
    print(premierNewPoint)
    print(deuxiemeNewPoint)
elif facette[5]<=0 and facette[8]>=0 and facette[11]<=0 :                                                      #seul le deuxieme point a son z>0
    memoirePointPositif = [facette[6],facette[7],facette[8]]
    premierNewPoint  = pointZ0([facette[6],facette[7],facette[8]],[facette[3],facette[4],facette[5]])
    deuxiemeNewPoint = pointZ0([facette[6],facette[7],facette[8]],[facette[9],facette[10],facette[11]])
    print(premierNewPoint)
    print(deuxiemeNewPoint)
elif facette[5]<=0 and facette[8]<=0 and facette[11]>=0 :                                                      #seul le dernier point a son z>0
    memoirePointPositif = [facette[9],facette[10],facette[11]]
    premierNewPoint  = pointZ0([facette[9],facette[10],facette[11]],[facette[3],facette[4],facette[5]])
    deuxiemeNewPoint = pointZ0([facette[9],facette[10],facette[11]],[facette[6],facette[7],facette[8]])
    print(premierNewPoint)
    print(deuxiemeNewPoint)
