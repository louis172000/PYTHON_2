import numpy as np

def Translate(translation, STL):
    for i in range(0, len(STL)):
        STL[i][5] += translation
        STL[i][8] += translation
        STL[i][11] += translation
    return STL

"""
Dans chaque liste de coordonées, respectivement, [normale, sommetA, sommetB, sommetC],
la coordonnées en z évolue positivement ou négativement.

Si la coordonnée diminue, le bateau tend à s'enfoncer
Si la coordonnée augmente le bateau tend à monter vres la surface
"""

def CompareForce(ForceArchimede, Poids):
    if ForceArchimede[2]<Poids[2]:
        print("le bateau s'enfonce")
    if ForceArchimede[2]>Poids[2]:
        print("le bateau sort de l'eau")
    if ForceArchimede[2]==Poids[2]:
        print("équilibre statique")


#print(Translate(4,liste_globale))
