class monome :
    def __init__(self, monome=None):
        ploynome = monome
        listestr = []
        liste = []
        L = None
        for i in ploynome:
            if i.isdigit():
                if L == None:
                    L = i
                else:
                    L += i
            if i.isdigit() == False:
                if L is not None:
                    listestr.append(L)      # cette boucle parcours la chaine de caractère et ajoute les NOMBRES à la listestr
                L = None
        listestr.append(L)
        for n in listestr:                  # convertit les str en float
            liste.append(float(n))
        print("liste complete : ", liste)
        monome = liste[:1]                  # pour faire un monome, on utilise les deux premiers termes
        self.__coeff = liste[0]
        self.__expo = liste[1]

    def getcoeff(self):
        return self.__coeff

    def getexpo(self):
        return self.__expo

    def setcoeff(self, value):
        self.coeff = value

    def setexpo(self, value):
        self.__expo = value

    def getcalcul(self, value):
        var = value**self.__expo * self.__coeff
        return var

    def print(self):
        print("coeff =", self.__coeff, "expo = ", self.__expo)

class polynome :
    def __init__(self, polynome=None):
        self.__racine = polynome

    def calcul_polynome(self, value):
        node = self.__racine                            # par la suite on utilisera la methode getcalcul en appelant la classe monome
        # print("getcoeff", node.getcoeff())

    def getracine(self):
        return self.__racine

    def add_first(self, d):
        self.__racine = monome(d, self.__racine)

    # def addpolynome(self, polynome):


obj1 = monome("4*x^2")
print("calcul :", obj1.getcalcul(1))
obj1.print()
L = polynome()
print(L.getracine())
L.calcul_polynome(2)
# L.add_first("8x^3")


print("---------------------------EXERCICE 2------------------------------")



class client:
    def __init__(self, nom, nextNode):
        self.__nom = nom
        self.__nextNode = nextNode

    def get_nom(self):
        return self.__nom

    def get_nextNode(self):
        return self.__nextNode

    def set_nom(self, nom):
        self.__nom = nom

    def set_nextNode(self, nextNode):
        self.__nextNode = nextNode

    def print(self):
        print(self.get_nom())
        print("pointe vers", self.get_nextNode())

class File:
    def __init__(self, racine=None):
        self.__racine = racine

    def add_first(self, d):
        self.__racine = client(d, self.__racine)

    def add_last(self, value):
        noeud = client(value, None)
        node = self.__racine
        if node is not None:
            while node.get_nextNode() is not None:
                node = node.get_nextNode()
            node.set_nextNode(noeud)
            print("ajout d'un client à la file")
        if node is None:
            node.set_nextNode(noeud)
            print("ajout du premier client à la file")

    def del_premier(self):
        premier_de_la_liste = self.__racine[0]
        self.__racine.remove(self.__racine[0])              # ne fonctionne pas car self.__racine n'est pas de forme liste
        return premier_de_la_liste

    def getracine(self):
        return self.__racine

    # def removeAsDeque(self):
    #     first = self.__racine[0]
    #     self.__racine.remove(self.__racine[0])
    #     return first

    def print(self):
        node = self.__racine
        if node is not None:
            numero_noeud = 1
            print("noeud", numero_noeud, ', nom = (', node.get_nom(), ') pointe vers -->', numero_noeud + 1 if node.get_nextNode() is not None else None)
            while node.get_nextNode() is not None:
                numero_noeud += 1
                node = node.get_nextNode()
                print("noeud", numero_noeud, ', nom = (',node.get_nom(), ') pointe vers -->',
                      numero_noeud + 1 if node.get_nextNode() is not None else None)
        else:
            print(node)


Clienta = client("Jean", 2)
Clientb = client("Matthieu", 1)
F = File()
F.add_first(Clienta)
F.add_last(Clientb)
F.print()
# print(F.removeAsDeque())
# print(F.removeAsDeque())
