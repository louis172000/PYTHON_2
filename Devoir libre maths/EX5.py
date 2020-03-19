"""
Jeu de roulette dans un casino
Somme détenue à la base : 10 000€
Probabilité de gagner : 18/37
On commence à miser 1€, si on perd on triple la mise
Si la somme détenue actuelle est <0 ou >20 000€, on arrête le jeu
On cherche la probabilité d'atteindre les 20 000€
Le jeu est-il favorable ?
"""

import numpy.random as rd
import matplotlib.pyplot as plt

probability_of_winning=18/37

repetitions=100000
x=[]
y=[]

for k in range(2,8):
    favorable=0
    x.append(k)
    for i in range(repetitions):
        balance=10000
        bet=1
        while balance>0 and balance<20000:
            balance-=bet
            if rd.binomial(1,probability_of_winning):
                balance+=2*bet
                bet=1
            else:
                bet*=3
        favorable+=1 if balance>20000 else 0
    y.append(favorable/repetitions)

plt.plot(x,y)
plt.title('Probabilité d\'atteindre 20 000€ avec un solde initial de 10 000€ en variant la mise')
plt.xlabel('Mise mulitiplé par')
plt.ylabel('Probabilité d\'atteindre 20 000€')
plt.show()
