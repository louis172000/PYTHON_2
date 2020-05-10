class duree:
    def __init__(self, heure, minute, seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde

    def __str__(self):
        return str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+"s"

    def __add__(self, autre):
        if isinstance(autre, duree) == True:
            min = 0
            h = 0
            seconde = self.__seconde+autre.__seconde
            if seconde >= 60:
                min += 1
                seconde -= 60
            min += self.__minute+autre.__minute
            if min >= 60:
                h +=1
                min -= 60
            h += self.__heure+autre.__heure
            return duree(h, min, seconde)
        else:
            print("Les 2 objets doivent être de la même classe")

if __name__== '__main__':
    c1 = duree(5, 54, 30)
    c2 = duree(5, 6, 34)
    c3 = c1 + c2
    print(c3)
