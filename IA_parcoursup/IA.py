import numpy as np
import matplotlib.pyplot as plt
from math import *
import csv

#av_prem = float(input("moyenne de l'annee de 1ere = "))
#av_term1 = float(input("moyenne du 1er trimestre de terminal = "))
#av_term2 = float(input("moyenne du 2eme trimestre de terminal = "))
#av_mp_prem = float(input("moyenne des spé (maths/physique) de premiere = "))
#av_mp_term1 = float(input("moyenne des spé (maths/physique) de terminal (1er trimestre) = "))
#av_mp_term2 = float(input("moyenne des spé (maths/physique) de terminal (2eme trimestre) = "))

def point_eleve():
    z = (1/(np.std([av_mp_prem, av_term1, av_term2])))**0.2
    print(z)
    s = (((av_prem + av_term1 + av_term2)/3) + 0.5*((av_mp_prem + av_mp_term1 + av_mp_term2)/3))/1.5
    return(s)

#print(point_eleve())

#oubliez pas de commenter le code, perso je déteste faire ca mais bon...

#j ai l impression que l utf-8 est pas supporté, pour avoir les key ect des dict faut ouvrir dans excel sinon ca prend en compte l utf-8

#ouverture des données opendata du gouvernement (dans le github)
with open('database/fr-esr-parcoursup_mpsi.csv', 'r') as fichier:
    data = []
    for row in csv.DictReader(fichier, delimiter= ';'):
        data.append(row)
    fichier.close()

#set up les colones que je veux garder
K = data[0].keys()
Keys_list = []
Keys_list_end = []

Keys_list_end.append('Session')
Keys_list_end.append('Ã‰tablissement')
Keys_list_end.append('Lien de la formation sur la plateforme Parcoursup')
Keys_list_end.append('CapacitÃ© de lâ€™Ã©tablissement par formation')
Keys_list_end.append('Effectif total des candidats pour une formation')
Keys_list_end.append('Effectif total des candidats ayant reÃ§u une proposition dâ€™admission de la part de lâ€™Ã©tablissement')
Keys_list_end.append('Effectif total des candidats ayant acceptÃ© la proposition de lâ€™Ã©tablissement (admis)')
Keys_list_end.append('Dont effectif des admis issus du mÃªme Ã©tablissement (BTS/CPGE)')
Keys_list_end.append('Dont effectif des admis issus de la mÃªme acadÃ©mie')
Keys_list_end.append('Rang du dernier appelÃ© du groupe 1')
Keys_list_end.append('Indicateur Parcoursup du taux dâ€™accÃ¨s des candidats ayant postulÃ© Ã  la formation (ratio entre le dernier appelÃ© et le dernier classÃ©)')

for i in K:
    Keys_list.append(i)

#supprimer celles que je veux pas
for i in range(len(Keys_list)):
    key = Keys_list[i]
    for w in range(len(Keys_list_end)):
        if key == Keys_list_end[w]:
            V = True
            break
        else:
            V = False
    if V == False:
        for n in range(len(data)):
            del data[n][key]

#debuggage
print(data[0].keys())
