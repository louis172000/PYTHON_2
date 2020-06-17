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

#Fonction pour déterminer la position d'équilibre
def f(x,Archimede,Poids):
    return int(Archimede[2])*x - int(Poids[2])

Archimede = [0,0,2]
Poids = [0,0,-5]
print(dichotomie(f,-100,100,0.001))

