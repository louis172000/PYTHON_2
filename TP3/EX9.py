def fonction(liste):
    listtriee = liste
    listtriee = sorted(listtriee)
    listtriee[0] = 0
    longueur = len(listtriee)
    del(listtriee[longueur-1])
    oddlist = []
    evenlist = []
    for i in range(0, longueur-1) :
        if liste[i] %2 ==0:
            evenlist.append(liste[i])
        else :
            oddlist.append(liste[i])
    return listtriee, oddlist, evenlist


liste = [4, 5, 6, 1, 7, 98, 32, 45, 61, 2, 9, 8, 6, 1, 5, 7]
triee, impairs, pairs = fonction(liste)

print("triée", triee)
print("impairs", impairs)
print("pairs", pairs)
