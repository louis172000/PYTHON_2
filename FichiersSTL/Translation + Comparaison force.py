import numpy as np

def Translate(translation, STL):
    for i in range(0, len(STL)):
        STL[i][5] = translation
        STL[i][8] = translation
        STL[i][11] = translation
    return STL


"""
Dans chaque liste de coordonées, respectivement, [normale, sommetA, sommetB, sommetC],
la coordonnées en z évolue positivement ou négativement.

Si la coordonnée diminue, le bateau tend à s'enfoncer
Si la coordonnée augmente le bateau tend à monter vres la surface
"""


def CompareForce(ForceArchimede, Poids):
    if ForceArchimede[2]-Poids[2] >0 and ForceArchimede[2]-Poids[2] < 0.001  :
        return "équilibre statique"
    if ForceArchimede[2] >= Poids[2] :
        return "le bateau s'enfonce"
    if ForceArchimede[2] <= Poids[2] :
        return "le bateau se soulève"

"""
On compare les normes des forces pour déterminer le point d'équilibre :

Si la norme de la poussée d'Archimède est environ égale à la norme du poids à un epsilon = 0.001 près,
alors il y a équilibre statique. 

Si la norme de la poussée d'Archimède est supérieure à la norme du poids à un epsilon = 0.001 près,
alors le bateau se soulève.

Si la norme de la poussée d'Archimède est inférieure à la norme du poids à un epsilon = 0.001 près,
alors le bateau s'enfonce.
"""


#print(CompareForce(ForceArchimede,Poids))
print(Translate(4,liste_globale))
