fichier = open("STL_Normals_Outward/Rectangular_HULL_Normals_Outward.STL")

############################################################################
#############             Definitions de fonctions             #############
############################################################################


def fonction_coordonnees_globales(liste, liste_triangle):
    liste = liste.split(" ")
    for i in range(0, len(liste)):
        liste[i] = float(liste[i])
        liste_triangle.append(liste[i])                 # ajoute les coordonnées (du type float) à la liste du triangle en question
    # print("liste :", liste)


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

    elif facette[5] <= 0 and facette[8] <= 0 and facette[11] <= 0:
        return [0, 0, 0]


def archimede(objet):
    somme = [0,0,0]
    for i in objet:
        interieurSomme = interieurSommeArchimede(i)
        somme = [somme[0]+interieurSomme[0], somme[1]+interieurSomme[1], somme[2]+interieurSomme[2]]
    rho = 1000
    g = 9.81
    pousseArchimede = [somme[0]*rho*g, somme[1]*rho*g, somme[2]*rho*g]

    return pousseArchimede

#Fonction dichotomie

def dichotomie(f,Zga,Zgb,eps):

    #Image des bornes de l'intervalle
    fZga = f(Zga,Archimede,Poids)
    fZgb = f(Zgb,Archimede,Poids)

    #Compteur d'itérations
    n = 0

    #On prend le milieu de l'intervalle à chaque tour de boucle, et on élimine la partie qui ne contient pas ce que l'on recherche
    while Zgb-Zga > eps :
        Zgm = (Zgb+Zga)/2
        fZgm = f(Zgm,Archimede,Poids)
        if fZga*fZgm < 0:
            Zgb = Zgm
            fZgb = fZgm
        else :
            Zga = Zgm
            fZga = fZgm
        n+=1
    print("Nombre d'itérations = ", n)
    return Zga


#Fonction pour trouver Zg, la position d'équilibre
def f(x,Archimede,Poids):
    return Archimede[2]*x - Poids[2]

#Définition du poids
def CalculPoids(masse):
    g = 9.81
    return [0,0,-masse*g]


objetEtudier = listeSTL(fichier)
print("objetEtudier :",objetEtudier)

Archimede = archimede(objetEtudier)
Poids = CalculPoids(40000)
print("Coordonnées du Poids =", Poids)
print("Coordonnées de la poussée d'Archimede =", Archimede)
print("Tirant d'eau =",abs(dichotomie(f,-100,100,0.001)))




