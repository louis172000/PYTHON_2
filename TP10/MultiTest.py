from TP10.Multinationale import multinationale
from TP10.Filiale import filiale
from TP10.Directeur import directeur
from TP10.Administratif import administratif
from TP10.Junior import junior
from TP10.Senior import senior


Multinationale = multinationale("CARS", "France")
# Multinationale.afficher()
print("------")

Filiale1 = filiale("CARS-Tunisie", "Tunisie", 1991, [])
Filiale2 = filiale("CARS-Belgique", "Belgique", 1992, [])
Filiale3 = filiale("CARS-Maroc", "Maroc", 1993, [])
Filiale4 = filiale("CARS-Angleterre", "Angleterre", 1994, [])


ing1 = directeur(2000, "Zuckerber", "Marc", 10, "appXI")
ing11 = senior("responsabilité", 200, 430, 2010, 3652, "jean", "bon", 5, "tortuga")
Filiale1.ajouter(ing1)
Filiale1.ajouter(ing11)
Multinationale.ajouter(Filiale1)
Multinationale.ajouter(Filiale2)
Multinationale.ajouter(Filiale3)
Multinationale.ajouter(Filiale4)

Multinationale.afficher()
Filiale1.afficher()
ing1.afficher()
ing11.afficher()
