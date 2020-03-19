from abc import ABC, abstractmethod


class salarie:
    def __init__(self, nom, prenom, ech_salaire, id):
        self._nom = nom
        self._prenom = prenom
        self._ech_salaire = ech_salaire
        self._id = id

    @abstractmethod
    def afficher(self):
        pass
