from src.Evenement import Evenement



class FinSimulation(Evenement):

    def __init__(self):
        super(FinSimulation, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.echeancier = []
        if simulateur.nbBus > 0:
            simulateur.TpsAttenteMoyControle = simulateur.histo.aireQc/simulateur.nbBus
        if simulateur.nbBusRep > 0:
            simulateur.TpsAttenteMoyReparation = simulateur.histo.aireQr/simulateur.nbBusRep

        simulateur.TauxUtilisationCentrereparation = simulateur.histo.aireBr/(2*simulateur.dureeMax)

