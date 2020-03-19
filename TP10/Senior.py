from TP10.Ingenieur import ingenieur

class senior(ingenieur):
    def __init__(self, resp, heure_projet, heure_gestion, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id):
        ingenieur.__init__(self, heure_projet, heure_gestion, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id)
        self.__resp = resp


    def afficher(self):
        print("[id=", self._id, "] Nom et Prénom : ", self._nom, " ", self._prenom, ", Salaire : ", self._ech_salaire,
               ", Statut : Directeur, Année de nomination : ", self._annee_embauche, "Site = ", "###########",
               "Nombre de jours de travails : ", self._nb_j_travail, ", Service, ", self.__resp)
