import numpy as np

class rational:
    def __init__(self, numerateur, denominateur):
        self.__numerateur = numerateur
        self.__denominateur = denominateur

    def __str__(self):
        return "=> "+str(self.__numerateur)+"/"+str(self.__denominateur)

    def __add__(self, autre):
        if isinstance(autre, rational) == True:
            num = self.__numerateur*autre.__denominateur+self.__denominateur*autre.__numerateur
            den = self.__denominateur*autre.__denominateur
            return rational(num, den)
        else:
            print("Les 2 objets doivent être de la même classe")

    def __sub__(self, autre):
        if isinstance(autre, rational) == True:
            num = self.__numerateur*autre.__denominateur-self.__denominateur*autre.__numerateur
            den = self.__denominateur*autre.__denominateur
            return rational(num, den)
        else:
            print("Les 2 objets doivent être de la même classe")


if __name__== '__main__':
    c1 = rational(8, 9)
    c2 = rational(5, 4)
    c3 = c1 + c2
    print(c3)
    c4 = c1 - c2
    print(c4)
