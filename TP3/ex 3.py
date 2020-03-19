def fct(val):
    if type(val) is int:
        print("c'est un entier")
        return
    elif type(val) is float:
        print("un nb reel")
        return
    elif type(val) is str:
        print("chaine de caracteres")
        return


print("entrez qqch")
valeur_a_determiner = eval(input())

fct(valeur_a_determiner)
