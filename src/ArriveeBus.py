import  ArriveeFileC as ArriveeFileC
from Evenement import Evenement
from Maths import *

class ArriveeBus(Evenement):
    def __init__(self):
        super(ArriveeBus, self).__init__()

    def procedure(self):
        from Simulateur import Simulateur
        simulateur = Simulateur()
        # On ajoute l'evenement arriveeBus dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu + exp(1 / 2), self)
        # on incrémente le nombre de bus
        simulateur.nbBus = simulateur.nbBus + 1
        # On ajoute l'evenement arrivéeFileC dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu, ArriveeFileC.ArriveeFileC())