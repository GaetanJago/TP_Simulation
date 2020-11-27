from src.Evenement import Evenement
from src.Maths import *
import src.DepartControle as DepartControle
import src.Simulateur as Simulateur

class AccesControle(Evenement):

    def __init__(self):
        super(AccesControle, self).__init__()

    def procedure(self):

        simulateur = Simulateur.Simulateur()
        simulateur.qc -= 1
        simulateur.bc = 1
        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(1/4,13/12), DepartControle.DepartControle())
