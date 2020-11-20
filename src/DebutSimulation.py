from src.Evenement import Evenement
from src.ArriveeBus import ArriveeBus
from src.FinSimulation import FinSimulation
from src.Simulateur import Simulateur
from src.Maths import *

class DebutSimulation(Evenement):

    def __init__(self):
        pass #super?

    def procedure(self):
        simu = Simulateur()
        simu.nbBus = 0
        simu.nbBusRep = 0
        simu.histo.aireQc = 0
        simu.histo.aireQr = 0
        simu.histo.aireBr = 0
        simu.qc = 0
        simu.qr = 0
        simu.bc = 0
        simu.br = 0
        simu.ajouterEvenement(simu.dateSimu + exp(1/2),ArriveeBus())
        simu.ajouterEvenement(simu.dureeMax, FinSimulation())
