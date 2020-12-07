from src.Evenement import Evenement
from src.Maths import *
import src.DepartControle as DepartControle

class AccesControle(Evenement):

    def __init__(self):
        super(AccesControle, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.qc -= 1
        simulateur.bc = 1
        date = simulateur.dateSimu + uniforme(1/4,13/12)

        #calcul temps d'attente chaque bus [date sortie file C]
        simulateur.sortieBusC(date)

        simulateur.ajouterEvenement(date, DepartControle.DepartControle())