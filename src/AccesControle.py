from Evenement import Evenement
from Maths import *
import DepartControle as DepartControle

class AccesControle(Evenement):

    def __init__(self):
        super(AccesControle, self).__init__()

    def procedure(self):
        from Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.qc -= 1
        simulateur.bc = 1
        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(1/4,13/12), DepartControle.DepartControle())
