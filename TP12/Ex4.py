def listSum(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    else:
        n = L[0]+L[len(L)-1]    # additionne le dernier et le premier
        L[0] = n                # remplace le preier par l'addition des deux
        del L[len(L)-1]         # supprime le dernier
        return listSum(L)


print(listSum([]))  # 0
print(listSum([42]))  # 42
print(listSum([3,1,5,2]))  # 11
