from src.Evenement import Evenement
from src.Simulateur import Simulateur
from src.Maths import *


class AccesReparation (Evenement):


    def __init__(self):
        pass

    def procedure(self):
        simulateur = Simulateur()
        # on décrémente le nombre de bus
        simulateur.nbBus = simulateur.nbBus - 1
       #on réquisitionne un poste dans le centre de réparation
        simulateur.br = simulateur.br + 1
        # On ajoute l'evenement arriveeBus dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu + exp(1 / 2), self)
        #On ajoute l'evenement arrivéeFileC dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu, arriveeFileC())

