import os
from pathlib import Path
import glob


path = "E:\\Document"


def listdirectory(path):
    fichier = []
    l = glob.glob(path+'\\*')
    for i in l:
        if os.path.isdir(i): fichier.extend(listdirectory(i))
        else: fichier.append(i)
    return fichier


# print(os.path.getsize(path))

# taille = 0
# listefichiers = listdirectory(path)
# print(listefichiers)
# for i in listefichiers:
#     taille = taille + os.path.getsize(listefichiers[i])
# print(taille)
os.path.getsize('E\Worms versions.txt')
