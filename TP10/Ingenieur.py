from abc import ABC, abstractmethod
from TP10.Employe import employe


class ingenieur(employe):
    def __init__(self, heure_projet, heure_gestion, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id):
        employe.__init__(self, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id)
        self._heure_projet = heure_projet
        self._heure_gestion = heure_gestion

    @abstractmethod
    def afficher(self):
        pass
