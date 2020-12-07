import  src.ArriveeFileC as ArriveeFileC
from src.Evenement import Evenement
from src.Maths import *

class ArriveeBus(Evenement):
    def __init__(self):
        super(ArriveeBus, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        date = simulateur.dateSimu + exp(1 / 2)
        # On ajoute l'evenement arriveeBus dans l'échéancier
        simulateur.ajouterEvenement(date, self)

        # calcul temps d'attente chaque bus [date arrivée file C]
        simulateur.arriveeBusC(date)

        # on incrémente le nombre de bus
        simulateur.nbBus = simulateur.nbBus + 1
        # On ajoute l'evenement arrivéeFileC dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu, ArriveeFileC.ArriveeFileC())