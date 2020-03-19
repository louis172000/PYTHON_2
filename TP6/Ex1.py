class Equation:
    def __init__(self, a=0, b=0, c=0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = 0

    def setcoefficients(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getracines(self):
        print("l'équation est du type : ", self.__a, "XX +", self.__b, "X +", self.__c)
        if self.__a == 0:
            return "l'équation n'est pas du second degré"
        self.__delta = self.__b*self.__b-4*self.__a*self.__c
        if self.__delta < 0:
            print("l'équation pas de solution réelles", end="")
        elif self.__delta == 0:
            print("il y a une racine : ", end="")
            racine = (-self.__b-self.__delta**0.5)/2*self.__a
            # print(" racine = ", racine)
            return racine
        else:
            print("il y a deux racines réeles : ", end="")
            racine1 = (-self.__b-self.__delta**0.5)/2*self.__a
            racine2 = (-self.__b+self.__delta**0.5)/2*self.__a
            # print(" racine 1 = ", racine1, "\n racine 2 = ", racine2)
            return racine1, racine2


obj = Equation()
obj.setcoefficients(1, 9, 8)
print(obj.getracines())
