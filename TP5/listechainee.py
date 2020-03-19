def createNode(node_number, data, next):

    node_number = {node_number:{'data': data, "next": next}}
    return node_number


def isEmpty(L):
    if len(L) == 0:
        return True
    else:
        return False


def size(L):
    return len(L)

def printLinkedList(L):
    print(L)                            #?


#def find(data, L):
#    if data in L:
#        return True
#    else:
#        return False


#def add_first(data, L):
##################


def add_last(data, L):
    node_number = size(L)+1
    node_number = "node"+str(node_number)
    L1 = createNode(node_number, data, next)
    L.update(L1)
    print(L)


#def add_ind(data, L, ind):
    #L[ind]=L[ind+data]


#def remove(data, L):
   # i = L.index(data)
   # del(L[i])



data = 5
L = createNode("node1", data, "node2")
print(L)
add_last(25, L)
print(isEmpty(L))                       #isEmpty fonctionne
