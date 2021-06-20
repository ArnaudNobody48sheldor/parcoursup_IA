import numpy as np
import matplotlib.pyplot as plt
from math import *
import csv

with open('database/fr-esr-parcoursup_mpsi.csv', 'r') as fichier:
    data = []
    for row in csv.DictReader(fichier, delimiter= ';'):
        data.append(row)
    fichier.close()

for i in range(len(data)):
    print(data[i]['Ã‰tablissement'])
