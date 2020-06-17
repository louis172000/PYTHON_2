def dichotomie(f,k,Zkb):
    Zka = -k

    imageZka = f(Zka,Archimede,Poids)
    imageZkb = f(Zkb,Archimede,Poids)

    n = 0

    while Zka > 0.001 :
        Zk = (Zka+Zkb)/2
        imageZk = f(Zk,Archimede,Poids)
        if imageZka != 0 :
            Zka = Zk
            imageZka = imageZk
        else :
            Zkb = Zk
            imageZkb = Zk
            n+=1
    print ("Nombre d'itérations nécessaires :", n )
    return (Zka+Zkb)/2



#Fonction pour trouver Zg, la position d'équilibre
def f(x,Archimede,Poids):
    return int(Archimede[2])*x - int(Poids[2])

# Définition du poids
#def Poids(masse):
 #   g = 9.81
  #  return [0,0,-masse*g]

Archimede = [0,0,2]
Poids = [0,0,-5]
print(dichotomie(f,100,0))
