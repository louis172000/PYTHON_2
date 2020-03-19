from TP10.Salarie import salarie


class directeur(salarie):
    def __init__(self, annee_nomination, nom, prenom, ech_salaire, id):
        salarie.__init__(self, nom, prenom, ech_salaire, id)
        self.__annee_nomination = annee_nomination

    def afficher(self):
        print("[id=", self._id, "] Nom et Prénom : ", self._nom, " ", self._prenom, ", Salaire : ", self._ech_salaire, ", Statut : Directeur, Année de nomination : ",
              self.__annee_nomination, "Site = ", "###########")
