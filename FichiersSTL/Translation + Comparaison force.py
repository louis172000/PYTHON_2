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
    if int(ForceArchimede[2])<0.001 and int(Poids[2])<0.001 :
        return "équilibre statique"
    if int(ForceArchimede[2])+int(Poids[2]) < 0.001:
        return "le bateau s'enfonce"
    if int(ForceArchimede[2])+int(Poids[2]) > 0.001:
        return "le bateau se soulève"



Poids = [0,0,-3]
ForceArchimede = [0,0,5]
print(CompareForce(ForceArchimede,Poids))
#print(Translate(4,liste_globale))
