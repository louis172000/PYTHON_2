############################################################################
############   Test de la fonction de la poussée d'Archimède   #############
############################################################################


############### fonctions générales ###############

def fonction_coordonnees_globales(liste, liste_triangle):
    liste = liste.split(" ")
    for i in range(0, len(liste)):
        liste[i] = float(liste[i])
        liste_triangle.append(liste[i])                 # ajoute les coordonnées (du type float) à la liste du triangle en question


def listeSTL(fichier):
    # ouverture fichier + insertion des lignes dans une liste : nb_triangle
    ligne = fichier.readlines()
    # supprime le premier et dernier élément extrait du fichier STL
    del ligne[0]
    del ligne[-1]

    nb_triangles = int(len(ligne)/7)

    liste_globale = []
    liste_triangle = []
    # récupération des coordonnées d'un triangle + sa normale et l'inclue dans la liste globale
    for iteration in range(0, nb_triangles):
        fin_de_lignenormale = (ligne[0+7*iteration])[15:]                   # récupère les derniers éléments de la ligne
        fonction_coordonnees_globales(fin_de_lignenormale, liste_triangle)
        fin_de_ligne_a = (ligne[2+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_a, liste_triangle)
        fin_de_ligne_b = (ligne[3+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_b, liste_triangle)
        fin_de_ligne_c = (ligne[4+7*iteration])[13:]
        fonction_coordonnees_globales(fin_de_ligne_c, liste_triangle)

        liste_globale.append(liste_triangle)
        # la liste_triangle à été ajoutée à liste_globale
        # on vide la liste triangle pour la calcul du triangle suivant
        liste_triangle = []

    return liste_globale



def pointZ0(a,b):
    if a[2]!= b[2]:
        xC = ((a[2]*b[0])-(b[2]*a[0]))/(a[2]-b[2])
        yC = ((a[1]*b[2])-(a[2]*b[1]))/(b[2]-a[2])
        return [xC,yC,0]
    else:
        return [0,0,0]


def Translate(translation, STL):
    for i in range(0, len(STL)):
        STL[i][5] += translation
        STL[i][8] += translation
        STL[i][11] += translation
    return STL


############### fonction de la poussée d'Archimède ###############

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


############################################################################
############   Test de la fonction de la poussée d'Archimède   #############
############################################################################


fichier = open("FichiersSTL/Rectangular_HULL_Normals_Outward.stl")
objetEtudie = listeSTL(fichier)
Translate(-0.25,objetEtudie)
print("poussée d'archimède maximale",archimede(objetEtudie))

