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

    def __str__(self):
        return self.__val


"""

node : c'est le noeud et left right sont les prochains noeuds -> voir liste chainées ??? 

"""


class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def get_root(self):
        return self.__root

    def is_root(self, node):
        if self.__root == node:
            return True
        else:
            return False

    def size(self, node):
        if node is None:
            return 0

        else:
            return self.size(node.get_left()) + 1 + self.size(node.get_right())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.get_left()) + self.printValues(node.get_right()) + " " + str(node.get_val())

    def sumValues(self, node):
        if node is None:
            return int(0)
        else:
            return self.sumValues(node.get_left()) + self.sumValues(node.get_right()) + int(node.get_val())

    def numberLeaves(self, node):
        if node is None:
            return 0
        if node.get_left() is None and node.get_right() is None:
            return 1
        else:
            return self.numberLeaves(node.get_left()) + self.numberLeaves(node.get_right())

    def numberInternalNode(self, node):
        if node is None:
            return 0
        if (node.get_left() is not None) or (node.get_right() is not None):
            return self.numberInternalNode(node.get_left()) + self.numberInternalNode(node.get_right()) + 1
        else:
            return 0

    def height(self, node):
        if node is None:
            return 0
        return max(self.size(node.get_left()), self.size(node.get_right()))-1

    def belongso(self, node, val):
        if node is None:
            return 0
        if node.get_val == val:
            return 1
        else:
            return self.belongs(node.get_left(), val), self.belongs(node.get_right(), val)

    def belongs(self, node, val):
        if node is None:
            return False
        if node.get_val() != val:
            return self.belongs(node.get_right(), val) or self.belongs(node.get_left(), val)
        else:
            return "Cette valeur appartient à l'arbre"

node3 = Node(3, None, None)
node4 = Node(4, None, node3)
node6 = Node(6, None, None)
node5 = Node(5, node6, node4)

node18 = Node(18, None, None)
node21 = Node(21, None, None)
node19 = Node(19, node21, node18)
node17 = Node(17, node19, None)

node12 = Node(12, node17, node5)

root = BinaryTree(node12)

# print(root.size(node12))
# print(root.printValues(node12))
# print(root.sumValues(node12))
# print(root.numberLeaves(node12))
# print(root.numberInternalNode(node12))
# print(root.height(node12))
# print(root.belongs(node12, 18))