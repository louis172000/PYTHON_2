class Node:
    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def get_val(self):
        return self.__val

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def set_right(self, new_right):
        self.__right = new_right

    def set_left(self, new_left):
        self.__left = new_left

"""
node : c'est le noeud et left right sont les prochains noeuds -> voir liste chainées ??? 

"""

class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def get_root(self):
        return self.__root


node3 = Node(3, None, None)
node4 = Node(4,None, node3)
node6 = Node(6, None, None)
node5 = Node(5, node6, node4)

node18 = Node(18, None, None)
node21 = Node(21, None, None)
node19 = Node(19, node21, node18)
node17 = Node(17, node19, None)

node12 = Node(12, node17, node5)

root = BinaryTree(node12)
