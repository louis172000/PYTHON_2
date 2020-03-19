from pile import *
filehandle = open('workfile', 'r+')
writewf2 = open('workfile2', 'w')
listoflines = filehandle.readlines()
linesoflist = len(listoflines)
print("le fichier contient", linesoflist, " lignes :")
print(listoflines)
filehandle.close()

for n in range(0, linesoflist):
    writewf2.write(pop(listoflines))

filehandle.close()
writewf2.close()
