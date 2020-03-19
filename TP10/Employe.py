from TP10.Salarie import salarie
from abc import ABC, abstractmethod


class employe(salarie):
    def __init__(self, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id):
        salarie.__init__(self, nom, prenom, ech_salaire, id)
        self._annee_embauche = annee_embauche
        self._nb_j_travail = nb_j_travail

    @abstractmethod
    def afficher(self):
        pass
