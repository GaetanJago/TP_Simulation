"""Module contenant diverses fonctions mathématique nécessaires au TP"""
from random import random
from math import *


# méthode modélisant une loi uniforme sur [borneInf, borneSup]
def uniforme(borneInf, borneSup):
    try:
        assert borneInf < borneSup
        return borneInf + (borneSup - borneInf) * random()
    except AssertionError:
        print("la borne inf doit être < à la borne sup")

# méthode modélisant une loi exponentielle de paramètre nombre en utilisant la propriété disant que si la variable U
# suit une loi uniforme sur [0,1] alors -(1/e)*ln(U) suit la loi exponentielle de paramètre e
def exp(parametre):
    try:
        assert parametre > 0
        return -(1 / parametre) * log(uniforme(0, 1))
    except AssertionError:
        print("Le paramètre de la loi exponentielle doit être >0")


# méthode permettant de modeliser le besoin de réparations sur un bus suivant la loi uniforme sur [0,1]
def generateRandom30():
    if random() < 0.3:
        return True
    else:
        return False
