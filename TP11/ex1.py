class cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def __add__(self, autre):
        if isinstance(autre, cercle) == True:
            return cercle(self.__rayon + autre.__rayon)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __gt__(self, autre):
        if isinstance(autre, cercle) == True:
            return self.__rayon < autre.__rayon
        else:
            print("Les 2 objets doivent être de la même class")

    def __lt__(self, autre):
        if isinstance(autre, cercle) == True:
            return self.__rayon > autre.__rayon
        else:
            print("Les 2 objets doivent être de la même class")

    def __str__(self):
        return "Rayon : x="+str(self.__rayon)


if __name__=='__main__':
    c1 = cercle(2)
    c2 = cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
