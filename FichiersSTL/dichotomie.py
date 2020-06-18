#Fonction dichotomie

def dichotomie(f,Zga,Zgb,eps,masse,STL):

    Archimede = archimede(STL)

    #Détermination du Poids en fonction de la masse et de g
    g = 9.81
    Poids = [0,0,-masse*g]

    #Image des bornes de l'intervalle
    fZga = f(Zga,Archimede,Poids)
    fZgb = f(Zgb,Archimede,Poids)

    #Compteur d'itérations
    n = 0
    #Création d'une liste des itérations qui serviront d'abscisses pour le graphique
    listeIteration = []

    #Création d'une liste des coordonnées qui serviront d'ordonnées pour le graphique
    listeCoordonneesZ = []

    #On prend le milieu de l'intervalle à chaque tour de boucle, et on élimine la partie qui ne contient pas ce que l'on recherche
    while Zgb-Zga > eps :
        Zgm = (Zgb+Zga)/2
        fZgm = f(Zgm,Archimede,Poids)
        if fZga*fZgm < 0:
            Zgb = Zgm
            #print(Zgm)
            fZgb = fZgm
            #print(Zgm)
        else :
            Zga = Zgm
            #print(Zgm)
            fZga = fZgm
        #print(Translate(Zgm,STL))
        #print(Zgm)

        #Ajout de l'itération à chaque tour de boucle
        listeIteration.append(n)

        #Ajout de Zgm à chaque tour de boucle
        listeCoordonneesZ.append(Zgm)
        n+=1
    #print("Nombre d'itérations = ", n)
    del listeIteration[0]
    del listeCoordonneesZ[0]
    return Zga,listeIteration,listeCoordonneesZ


#Fonction pour trouver Zg, la position d'équilibre
def f(x,Archimede,Poids):
    return Archimede[2]*x - Poids[2]
