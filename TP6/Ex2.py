class Rational:
    def __init__(self, num=0, den=1):
        self.__num = num
        self.__den = den

    def __getPGCD(self):
        a = self.__num
        b = self.__den
        reste = a % b
        while reste != 0:
            a = b
            b = reste
            reste = a % b
        return b

    def __getPPCM(self):
        a = self.__num
        b = self.__den
        ppcm = a*b/self.__getPGCD()
        return ppcm

    def set_den_egal_zero(self, num, den):
        if self.__den == 0:
            return "denominateur égal à zéro"
        else:
            self.__num = num
            self.__den = den

    def get_num_den(self):
        return self.__num, self.__den

    def affichagefraction(self):
        print(self.__num, "/", self.__den)

    def simplification_fraction(self):
        pgcd = self.__getPGCD()
        self.__num /= pgcd
        self.__den /= pgcd
        return str(self.__num) + "/" + str(self.__den)

    def fractions_egales(self, a, b):
        fraction1 = a.simplification_fraction()
        fraction2 = b.simplification_fraction()
        if fraction1 == fraction2:
            return "les fractions sont égales"
        else:
            return "les fractions sont différentes"

    def produit_fractions(self, a, b):
        num = a.__num * b.__num
        den = a.__den * b.__den
        f = Rational(num, den)
        return f.affichagefraction()

    def division_fractions(self, a, b):
        num = a.__num / b.__num
        den = a.__den / b.__den
        a = Rational(num, den)
        return a.affichagefraction()

    def addition_fraction(self,a , b):
        ppcm_a = float(a.__getPPCM())
        ppcm_b = float(b.__getPPCM())
        ppcm_ab = ppcm_a*ppcm_b
        num = a.__num*ppcm_ab/a.__den + b.__num*ppcm_ab/b.__den
        den = float(ppcm_ab)
        obj50 = Rational(num, den)
        obj50.simplification_fraction()
        return obj50.affichagefraction()


obj1 = Rational(2, 1)
obj2 = Rational(4, 2)
print("premier objet  : ", obj1.get_num_den(), "\ndeuxieme objet : ", obj2.get_num_den())
print("----------------------------")
print("affichage fractions simplifiée egales ?\nobj1 = ", obj1.simplification_fraction())
print("obj2 = ", obj2.simplification_fraction())
print(obj1.fractions_egales(obj1, obj2))
print("----------------------------")
print("produit : ", obj1.produit_fractions(obj1, obj2))
print("divison : ", obj1.division_fractions(obj1, obj2))
print("adddition simplifiée : ", obj1.addition_fraction(obj1, obj2))
