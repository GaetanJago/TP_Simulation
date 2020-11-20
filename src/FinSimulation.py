from src.Evenement import Evenement
from src.Simulateur import Simulateur


class FinSimulation(Evenement):

    def __init__(self):
        super(FinSimulation, self).__init__()

    def procedure(self):
        simulateur = Simulateur()
        simulateur.echeancier = []
        simulateur.TpsAttenteMoyControle = simulateur.histo.aireQc/simulateur.nbBus
        simulateur.TpsAttenteMoyReparation = simulateur.histo.aireQr/simulateur.nbBusRep
        simulateur.TauxUtilisationCentrereparation = simulateur.histo.aireBr/(2*simulateur.dureeMax)

