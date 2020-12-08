import  src.ArriveeFileC as ArriveeFileC
from src.Evenement import Evenement
from src.Maths import *
import src.Simulateur as Simulateur


class ArriveeBus(Evenement):
    def __init__(self):
        super(ArriveeBus, self).__init__()

    def procedure(self):

        simulateur = Simulateur.Simulateur()
        # On ajoute l'evenement arriveeBus dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu + exp(1 / 2), self)
        # on incrémente le nombre de bus
        simulateur.nbBus = simulateur.nbBus + 1

        #On insere la date a laquelle le bus est arrive dans l'histo
        simulateur.histo.datesArriveeBus.append(simulateur.dateSimu)

        # On ajoute l'evenement arrivéeFileC dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu, ArriveeFileC.ArriveeFileC())