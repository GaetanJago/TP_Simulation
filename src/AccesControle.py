from src.Evenement import Evenement
from src.Simulateur import Simulateur
from src.Maths import *

class AccesControle(Evenement):

    def __init__(self):
        pass

    def procedure(self):
        simulateur = Simulateur()
        simulateur.qc -= 1
        simulateur.bc = 1
        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(1/4,13/12), DepartControle())
