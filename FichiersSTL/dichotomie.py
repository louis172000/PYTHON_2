import numpy as np

#Fonction dichotomie

def dichotomie (f,a,b):
    #Bornes de base
    maximumIntervalle = max(a,b)
    minimumIntervalle = min(a,b)

    #Image des bornes
    imageDuMin = f(minimumIntervalle,Archimede,Poids)
    imageDuMax = f(maximumIntervalle,Archimede,Poids)

    #Compteur d'itérations
    n = 0

    #On prend le milieu de l'intervalle à chaque tour de boucle, et on élimine la partie qui ne contient pas ce que l'on recherche
    while maximumIntervalle-minimumIntervalle > 0.001:
        Zg = (maximumIntervalle+minimumIntervalle)/2
        imageZg = f(Zg,Archimede,Poids)
        if (imageDuMin > 0 and imageZg < 0) or (imageDuMin < 0 and imageZg > 0):
            maximumIntervalle = Zg
            imageDuMax = imageZg
        else :
            minimumIntervalle = Zg
            imageDuMin = imageZg
            #print(imageZg)
            n += 1
    print ("nombre d'itérations nécessaires :", n )
    return (maximumIntervalle+minimumIntervalle)/2

#Fonction pour trouver Zg, la position d'équilibre
def f(x,Archimede,Poids):
    return int(Archimede[2])*x - int(Poids[2])

Archimede = [0,0,2]
Poids = [0,0,-5]
print(dichotomie(f,-100,100))
