import numpy as np
import matplotlib.pyplot as plt
from math import *
import csv

#oubliez pas de comenter le code, perso je déteste faire ca mais bon...

#j ai l impression que l utf-8 est pas supporté, pour avoir les key ect des dict faut ouvrir dans excel sinon ca prend en compte l utf-8

with open('database/fr-esr-parcoursup_mpsi.csv', 'r') as fichier:
    data = []
    for row in csv.DictReader(fichier, delimiter= ';'):
        data.append(row)
    fichier.close()

print(" ")
print(" ")
print(" ")
print(" ")

DATA = []

for i in range(len(data)):
    DATA.append(data[i]['Session'])
    DATA.append(data[i]['Ã‰tablissement'])
    DATA.append(data[i]['Lien de la formation sur la plateforme Parcoursup'])
    DATA.append(data[i]['CapacitÃ© de lâ€™Ã©tablissement par formation'])
    DATA.append(data[i]['Effectif total des candidats pour une formation'])
    DATA.append(data[i]['Effectif total des candidats ayant reÃ§u une proposition dâ€™admission de la part de lâ€™Ã©tablissement'])
    DATA.append(data[i]['Effectif total des candidats ayant acceptÃ© la proposition de lâ€™Ã©tablissement (admis)'])
    DATA.append(data[i]['Dont effectif des admis issus du mÃªme Ã©tablissement (BTS/CPGE)'])
    DATA.append(data[i]['Dont effectif des admis issus de la mÃªme acadÃ©mie'])
    DATA.append(data[i]['Rang du dernier appelÃ© du groupe 1'])
    DATA.append(data[i]['Indicateur Parcoursup du taux dâ€™accÃ¨s des candidats ayant postulÃ© Ã  la formation (ratio entre le dernier appelÃ© et le dernier classÃ©)'])


K = data[0].keys()
Keys_list = []

for i in K:
    Keys_list.append(i)

print(Keys_list)
