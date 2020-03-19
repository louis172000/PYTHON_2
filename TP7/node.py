class Node:
    def __init__(self, data, nextNode):
        self.__data = data
        self.__nextNode = nextNode

    def get_data(self):
        return self.__data

    def get_nextNode(self):
        return self.__nextNode

    def set_data(self, data):
        self.__data = data

    def set_nextNode(self, nextNode):
        self.__nextNode = nextNode

    def print(self):
        print(self.get_data())
        print("pointe vers", self.get_nextNode())


obj1 = Node("elephant", "node2")
# obj2 = node("arc-en-ciel", "node4")
obj1.print()
# obj2.print()
