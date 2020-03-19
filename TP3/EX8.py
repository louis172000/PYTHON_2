def fct(l, string1):
    string1 = string1.lower()
    print("chaine de base :", string1)
    n = len(string1)
    print(n)
    newstring = ""
    nb = n-1
    compteur = 0
    for i in range (0, n):
        newstring += string1[nb]
        if l == string1[nb]:
            compteur += 1
        nb -= 1
    print("chaine inversée :", newstring)
    print("nb de lettres", l, ":", compteur)
    return compteur, newstring


lettre, mot = "e", "eCOLE"
fct(lettre, mot)
