from src.Evenement import Evenement
from src.Simulateur import Simulateur


class FinSimulation(Evenement):

    def __init__(self):
        pass

    def procedure(self):
        simulateur = Simulateur()
        simulateur.echeancier = []

