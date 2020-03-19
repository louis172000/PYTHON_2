def moyenne(list):
    n = len(list)
    nbmoy = 0
    """calcul de la moyenne de n notes"""
    for i in range(0, n-1):
        # print(current)
        nbmoy += list[i]
    moy = nbmoy/n
    return moy


notes = [5, 6, 15, 13, 10, 20, 1]
moyenne = moyenne(notes)
moyenne = float(int(moyenne*1000))/1000
print(moyenne)
