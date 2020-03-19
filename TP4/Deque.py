class Deque:
    def __init__(self, elements=[]):
        self.__elements = elements

    def insertAsStack(self, element):
        self.__elements.append(element)

    def insertAsQueue(self, element):
        self.__elements.insert(0, element)

    def removeAsStack(self):
        self.__elements.pop()

    def removeAsQueue(self):
        self.__elements.pop()

    def removeAsDeque(self):
        self.__elements.remove(self.__elements[0])

    def print(self):
        print(self.__elements)


d = Deque([1, 2])
d.insertAsQueue(5)
d.insertAsQueue(6)
d.insertAsQueue(7)
d.insertAsStack(8)
d.print()




