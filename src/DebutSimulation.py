from src.Evenement import Evenement
import  src.ArriveeBus as ArriveeBus
import  src.FinSimulation as FinSimulation
from src.Maths import *

class DebutSimulation(Evenement):

    def __init__(self):
        super(DebutSimulation, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
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
        simu.ajouterEvenement(simu.dateSimu + exp(1/2),ArriveeBus.ArriveeBus())
        simu.ajouterEvenement(simu.dureeMax, FinSimulation.FinSimulation())
