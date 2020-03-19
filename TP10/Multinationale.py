from abc import ABC, abstractmethod
from TP10.Filiale import filiale


class multinationale:
    def __init__(self, nom, pays_origine, list_filiale=[]):
        self.__nom = nom
        self.__pays_origine = pays_origine
        self.__list_filiale = list_filiale

    def ajouter(self, filiale):
        self.__list_filiale.append(filiale)


    def afficher(self):
        print("- La multinationale", self.__nom, "est composé de", len(self.__list_filiale), "filiales. D'origine est la", self.__pays_origine, ".")
        for i in range(0, len(self.__list_filiale)):
            d = self.__list_filiale[0]
            date = d.get_date()
            c = self.__list_filiale[i]
            date1 = self.__list_filiale[i].get_date()
            if date1 < date:
                self.__list_filiale[0] = c
                self.__list_filiale[i] = d
        a = self.__list_filiale[0].get_nom()
        print("La filiale la plus ancienne de cette multinationale est : ", a, end= "")
        print(" . Elle est comstitué de ", len(self._salarie), " salarie. ")                # envoyer le parametre de filiale dans Multinationale
        nb_salarie = 0
        for i in range(0, len(self.__list_filiale)):
            nb_salarie += self.__list_filiale[i].get_nb_salarie()
        print("- ", self.__nom, "est composée de ", nb_salarie, " salarie au total")
