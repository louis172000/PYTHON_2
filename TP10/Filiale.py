from TP10.Salarie import salarie


class filiale:
    def __init__(self, nom, pays, date_creation, salaries=[]):
        self._nom = nom
        self._date_creation = date_creation
        self._salarie = salaries
        self._pays = pays

    def ajouter(self, salarie):
        self._salarie.append(salarie)

    def supprimer(self, salarie):
        self._salarie.remove(salarie)

    def get_date(self):
        return self._date_creation

    def get_nom(self):
        return self._nom

    def get_nb_salarie(self):
        return len(self._salarie)

    def afficher(self):
        print(" . Elle est comstitué de ", len(self._salarie), " salarie. ")

