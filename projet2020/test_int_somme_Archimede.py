def interieurSommeArchimede(facette):                                                              #Calcul de l'intérieur de la somme de la formule d'Archimède

    if facette[5]<=0 and facette[8]<=0 and facette[11]<=0 :                                                        #si la facette est imergée, on calcul la pression de l'eau sur celle-ci
        ab = [facette[6]-facette[3],facette[7]-facette[4],facette[8]-facette[5]]
        ac = [facette[9]-facette[3],facette[10]-facette[4],facette[11]-facette[5]]
        ab_scalaire_ac = [ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        normeScalaireSurDeux = (((ab_scalaire_ac[0]**2)+(ab_scalaire_ac[1]**2)+(ab_scalaire_ac[2]**2))**(1/2))/2
        surfaceSurNormale = [normeScalaireSurDeux*facette[0],normeScalaireSurDeux*facette[1],normeScalaireSurDeux*facette[2]]
        z = (facette[5]+facette[8]+facette[11])/3
        interieurSomme = [surfaceSurNormale[0]*z,surfaceSurNormale[1]*z,surfaceSurNormale[2]*z]
        return interieurSomme

    elif facette[5]>=0 and facette[8]>=0 and facette[11]>=0 :                                                      #si la facette n'est pas imergée, on ne calcul pas la pression de l'eau sur celle-ci
        return [0,0,0]

#test
fichier = open("FichiersSTL/une_facette.stl")
def listeSTL(fichier):
    ligne = fichier.readlines()
    del ligne[0]
    del ligne[-1]
    nb_triangles = int(len(ligne)/7)

    liste_globale = []
    liste_triangle = []

    for iteration in range(0, nb_triangles):
        fin_de_lignenormale = (ligne[0+7*iteration])[15:]
        fin_de_lignenormale = fin_de_lignenormale.split(" ")
        for i in range(0, len(fin_de_lignenormale)):
            fin_de_lignenormale[i] = float(fin_de_lignenormale[i])
            liste_triangle.append(fin_de_lignenormale[i])

        fin_de_ligneA = (ligne[2+7*iteration])[13:]
        fin_de_ligneA = fin_de_ligneA.split(" ")
        for i in range(0, len(fin_de_ligneA)):
            fin_de_ligneA[i] = float(fin_de_ligneA[i])
            liste_triangle.append(fin_de_ligneA[i])

        fin_de_ligneB = (ligne[3+7*iteration])[13:]
        fin_de_ligneB = fin_de_ligneB.split(" ")
        for i in range(0, len(fin_de_ligneB)):
            fin_de_ligneB[i] = float(fin_de_ligneB[i])
            liste_triangle.append(fin_de_ligneB[i])

        fin_de_ligneC = (ligne[4+7*iteration])[13:]
        fin_de_ligneC = fin_de_ligneC.split(" ")
        for i in range(0, len(fin_de_ligneC)):
            fin_de_ligneC[i] = float(fin_de_ligneC[i])
            liste_triangle.append(fin_de_ligneC[i])

        liste_globale.append(liste_triangle)
        # la liste_triangle à été ajoutée
        liste_triangle = []
    return liste_globale

objetEtudier = listeSTL(fichier)
print(objetEtudier)
print(interieurSommeArchimede(objetEtudier[0]))
