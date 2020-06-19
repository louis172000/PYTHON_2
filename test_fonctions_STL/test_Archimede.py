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
    print("Structure composée de :", nb_triangles, "triangles")
    print("""Classée de la façon suivante: 
liste_globale = [coordonées du triangle1 (type:liste), coordonées du triangle2 (type:liste), ...]
""")
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



def interieurSommeArchimede(facette):
    if facette[5] >= 0 and facette[8] >= 0 and facette[11] >= 0:
        ab = [facette[6]-facette[3], facette[7]-facette[4], facette[8]-facette[5]]
        ac = [facette[9]-facette[3], facette[10]-facette[4], facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1], ab[2]*ac[0]-ab[0]*ac[2], ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceParNormale = [normeScalaireSurDeux*facette[0], normeScalaireSurDeux*facette[1], normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        interieurSomme = [surfaceParNormale[0]*z, surfaceParNormale[1]*z, surfaceParNormale[2]*z]
        return interieurSomme

    else :
        return [0, 0, 0]


############### fonction de la poussée d'Archimède ###############

def archimede(objet):
    somme = [0,0,0]
    for i in objet:
        interieurSomme = interieurSommeArchimede(i)
        somme = [somme[0]+interieurSomme[0], somme[1]+interieurSomme[1], somme[2]+interieurSomme[2]]
    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g, somme[1]*rho*g, somme[2]*rho*g]

    return pousseArchimede

############################################################################
#############                   Main program                   #############
############################################################################

fichier = open("FichiersSTL/Rectangular_HULL_Normals_Outward.stl")
objetEtudie = listeSTL(fichier)
print("Objet Etudié :",objetEtudie)                                              #Il est possible que si le nombre de facette dépasse les 5500 l'affichage ne soit pas complet
print("poussée d'archimède maximale",archimede(objetEtudie))
