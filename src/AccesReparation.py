from src.DepartReparation import DepartReparation
from src.Evenement import Evenement
from src.Simulateur import Simulateur
from src.Maths import *


class AccesReparation (Evenement):


    def __init__(self):
        super(AccesReparation, self).__init__()

    def procedure(self):
        simulateur = Simulateur()
        #on décrémente le nombre de bus
        simulateur.nbBus = simulateur.nbBus - 1
        #on réquisitionne un poste dans le centre de réparation
        simulateur.br = simulateur.br + 1
        # On ajoute l'evenement DepartReparation dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(2.1, 4.5), DepartReparation())

