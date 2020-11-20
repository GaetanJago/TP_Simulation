from src.AccesControle import AccesControle
from src.ArriveeFileR import ArriveeFileR
from src.Evenement import Evenement
from src.Maths import generateRandom30
from src.Simulateur import Simulateur


class DebutSimulation(Evenement):

    def __init__(self):
        pass

    def procedure(self):
        simulateur = Simulateur()

        simulateur.bc = 0 # Changer le statut du centre de contrôle en libre

        # Si la file C est non vide
        if simulateur.qc > 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle())

        if generateRandom30() == True:
            simulateur.ajouterEvenement(simulateur.dateSimu, ArriveeFileR())

