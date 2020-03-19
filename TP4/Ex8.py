from pile import *
chaine = "5 1 2 + 4 * + 3 -"


def deque(chaine):
    pile = newstack()                           # creation nouvelle pile
    chaine = chaine.split(" ")
    print(chaine)
    for n in range(len(chaine)):
        if chaine[n].isdigit():                 # rempli la pile avec les nombres
            push(pile, chaine[n])
            print(pile)
        else:                                   # si c'est un operateur, ou applique le calcul entre les deus derniers chiffres de la liste0
            operator = chaine[n]
            val2 = pop(pile)
            val1 = pop(pile)
            #print(val1+operator+val2)
            nb = str(eval(val1+operator+val2))
            print(nb)
            push(pile, nb)


deque(chaine)
