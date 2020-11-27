import src.AccesControle as AccesControle
from src.Evenement import Evenement
import src.Simulateur as Simulateur

class ArriveeFileC(Evenement):

    def __init__(self):
        super(ArriveeFileC, self).__init__()

    def procedure(self):

        simulateur = Simulateur.Simulateur()
        simulateur.qc += 1
        if simulateur.bc == 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle.AccesControle())


