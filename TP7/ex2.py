from node import Node


class LinkedList:
    def __init__(self, racine=None):
        self.__racine = racine

    def add_first(self, d):
        self.__racine = Node(d, self.__racine)
        return 0

    def getracine(self):
        print(self.__racine)

    def add_last(self, value):
        noeud = Node(value, None)
        node = self.__racine
        if node is not None:
            while node.get_nextNode() is not None:
                node = node.get_nextNode()
            node.set_nextNode(noeud)
        return 0

    def add_after(self, prev, data):
        node = self.__racine
        if node is not None:
            numero_noeud = 1
            while numero_noeud != prev:
                numero_noeud += 1
                node = node.get_nextNode()
            noeud = Node(data, node.get_nextNode())
            node.set_nextNode(noeud)

    def print(self):
        node = self.__racine
        if node is not None:
            numero_noeud = 1
            print(numero_noeud, 'data = (' + str(node.get_data()) + ') -->', numero_noeud + 1 if node.get_nextNode() is not None else None)
            while node.get_nextNode() is not None:
                numero_noeud += 1
                node = node.get_nextNode()
                print(numero_noeud, 'data = (' + str(node.get_data()) + ') -->',
                      numero_noeud + 1 if node.get_nextNode() is not None else None)
        else:
            print(node)


L = LinkedList()
n1 = L.add_first(2)
n2 = L.add_first(1)
n3 = L.add_last(3)
L.print()
L.getracine()
print("------------------")
L.add_first(78)
L.add_first(78)
L.add_first(78)
L.add_first(78)
L.add_first(78)
L.add_first(7)
L.add_last(8)
L.add_first(9)
L.add_after(2, 90)

L.print()
