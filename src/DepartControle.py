import src.AccesControle as AccesControle
import src.ArriveeFileR as ArriveeFileR
from src.Evenement import Evenement
from src.Maths import generateRandom30
import src.Simulateur as Simulateur

class DepartControle(Evenement):

    def __init__(self):
        super(DepartControle, self).__init__()

    def procedure(self):

        simulateur = Simulateur.Simulateur()

        simulateur.bc = 0 # Changer le statut du centre de contrôle en libre

        # Si la file C est non vide
        if simulateur.qc > 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle.AccesControle())

        if generateRandom30() == True:
            simulateur.ajouterEvenement(simulateur.dateSimu, ArriveeFileR.ArriveeFileR())

