from abc import ABC, abstractmethod

class sapin:
    def __init__(self, masseMax = 5000, masseTotale = 0, decotab=[]):
        self.__masseMax = masseMax
        self.__masseTotale = masseTotale
        self.__decotab = decotab

    def ajouter(self, deco):
        self.__decotab.append(deco)
        self.__masseTotale += deco._masse

    def supprimer(self, deco):
        self.__decotab.remove(deco)
        self.__masseTotale -= deco._masse

    def afficher(self):
        print("Ce sapin de Noël peut supporter ", self.__masseMax, "g de décoration.")
        if self.__decotab == []:
            print("Il ne contient actuellement aucune decoration\n----")
        else:
            print("Il contient actuellement ", self.__masseTotale, "g de décoration, listée ci-après :")
            for i in self.__decotab:
                i.afficher()
        print("-------------------------------------------")




class deco:
    def __init__(self, couleur, masse):
        self._couleur = couleur
        self._masse = masse             # un tiret pour mettre la variable en protégé

    @abstractmethod
    def afficher(self):
        pass


class boule(deco):
    def __init__(self, couleur, masse,  diametre):
        deco.__init__(self, couleur, masse)
        self.__diametre = diametre

    def afficher(self):
        print("* Boule ", self._couleur," de ", self.__diametre, "cm de diametre, pesant ", self._masse, "g.")

class guirlande(deco):
    def __init__(self, couleur, masse, longueur):
        deco.__init__(self, couleur, masse)
        self._longueur = longueur

    def afficher(self):
        pass


class guirlandelumineuse(guirlande):
    def __init__(self, couleur, masse, longueur, nblumieres):
        guirlande.__init__(self, couleur, masse, longueur)
        self.__nblumieres = nblumieres

    def afficher(self):
        print("* Guirlande ", self._longueur,"cm de long, possédant ", self.__nblumieres," lumières et pesant ",self._masse, "g.")



sapin = sapin(5000, 0, [])
sapin.afficher()
print("==============")
boule1 = boule("rouge", 15, 5)
sapin.ajouter(boule1)
g = guirlandelumineuse("bleu", 200, 500, 5)
sapin.ajouter(g)
sapin.afficher()
print("==============")
sapin.supprimer(boule1)
sapin.afficher()
