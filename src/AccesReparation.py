import src.DepartReparation as DepartReparation
from src.Evenement import Evenement
from src.Maths import *


class AccesReparation (Evenement):


    def __init__(self):
        super(AccesReparation, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        #on décrémente le nombre de bus
        simulateur.qr = simulateur.qr - 1
        #on réquisitionne un poste dans le centre de réparation
        simulateur.br = simulateur.br + 1
        # On ajoute l'evenement DepartReparation dans l'échéancier
        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(2.1, 4.5), DepartReparation.DepartReparation())

