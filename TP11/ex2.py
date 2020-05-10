import numpy as np

class complex:
    def __init__(self, reel, imaginaire):
        self.__reel = reel
        self.__imaginaire = imaginaire


    def __str__(self):
        reel = "=> partie réelle     : "+str(self.__reel)
        img = "\n   partie imaginaire : "+str(self.__imaginaire)
        return reel+img


    def __add__(self, autre):
        if isinstance(autre, complex) == True:
            return complex(self.__reel + autre.__reel, self.__imaginaire + autre.__imaginaire)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __sub__(self, autre):
        if isinstance(autre, complex) == True:
            return complex(self.__reel - autre.__reel, self.__imaginaire - autre.__imaginaire)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __mul__(self, autre):
        if isinstance(autre, complex) == True:
            reel = self.__reel*autre.__reel-self.__imaginaire*autre.__imaginaire
            img = self.__reel*autre.__imaginaire + self.__imaginaire*autre.__reel
            return complex(reel, img)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __truediv__(self, autre):
        if isinstance(autre, complex) == True:
            reel = (self.__reel*autre.__reel + self.__imaginaire*autre.__imaginaire)/(autre.__reel**2+autre.__imaginaire**2)
            img = (self.__reel*autre.__imaginaire - self.__imaginaire*autre.__reel)/(autre.__reel**2+autre.__imaginaire**2)
            return complex(reel, img)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __abs__(self):
            val = np.sqrt(self.__reel**2 + self.__imaginaire**2)
            return complex(val, 0)

    def __eq__(self, autre):
        if isinstance(autre, complex) == True:
            i = "false"
            n = "false"
            if self.__reel == autre.__reel:
                i = "true"
            if self.__imaginaire == autre.__imaginaire:
                n = "true"
            if i and n == "true":
                print("les nombres complexes sont égaux")
                return True
            else:
                print("les nombres complexes sont différents")
        else:
            print("Les 2 objets doivent être de la même classe")

    def __ne__(self, autre):
        if isinstance(autre, complex) == True:
            i = "false"
            n = "false"
            if self.__reel != autre.__reel:
                i = "true"
            if self.__imaginaire != autre.__imaginaire:
                n = "true"
            if i and n == "true":
                print("les nombres complexes sont différents")
                return True
            else:
                print("les nombres complexes sont égaux")
        else:
            print("Les 2 objets doivent être de la même classe")

if __name__== '__main__':
    c1 = complex(2, 1)
    c2 = complex(3, 6)
    c3 = c1 + c2
    print(c3)
    c4 = c1 - c2
    print(c4)
    c5 = c2 * c3
    print(c5)
    c6 = c2 / c3
    print(c6)
    c7 = abs(c2)
    print(c7)
    c8 = c2 == c3
    print(c8)
    c9 = c2 != c3
    print(c9)
