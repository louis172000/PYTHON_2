import numpy.random as rd
liste = []
for j in range(1, 1000001):
    x = rd.randint(1, 7)
    y = rd.randint(1, 7)
    z = x+y
    liste.append(z)

gain = 0
for i in liste:
    if liste[i] == 2 or liste[i] == 12:
        gain += 2
    if liste[i] == 7:
        gain -= 1
    else :
        gain += 0
print(gain)
