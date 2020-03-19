from TP10.Employe import employe

class administratif(employe):
    def __init__(self, service_travail, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id):
        employe.__init__(self, annee_embauche, nb_j_travail, nom, prenom, ech_salaire, id)
        self.__service_travail = service_travail

    def afficher(self):
                print("[id=", self._id, "] Nom et Prénom : ", self._nom, " ", self._prenom, ", Salaire : ", self._ech_salaire,
                      ", Statut : Directeur, Année de nomination : ", self._annee_embauche, "Site = ", "###########",
                      "Nombre de jours de travails : ", self._nb_j_travail, ", Service, ", self.__service_travail)
