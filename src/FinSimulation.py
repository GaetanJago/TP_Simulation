from Evenement import Evenement

class FinSimulation(Evenement):

    def __init__(self):
        super(FinSimulation, self).__init__()

    def procedure(self):
        from Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.echeancier = []
        if simulateur.nbBus > 0:
            simulateur.TpsAttenteMoyControle = simulateur.histo.aireQc/simulateur.nbBus
            if simulateur.qc > 0:
                simulateur.TpsAttenteMoyenControleExcluentBusAttente = (simulateur.histo.aireQc -
                (simulateur.dateSimulationC[len(simulateur.dateSimulationC)-1]-simulateur.dateSimulationC[len(simulateur.dateSimulationC)-simulateur.qc])*simulateur.qc)/(simulateur.nbBus - simulateur.qc)
        if simulateur.nbBusRep > 0:
            simulateur.TpsAttenteMoyReparation = simulateur.histo.aireQr/simulateur.nbBusRep
            if(simulateur.qr > 0):
                simulateur.TpsAttenteMoyenReparationExcluentBusAttente = (simulateur.histo.aireQr -
                (simulateur.dateSimulationR[len(simulateur.dateSimulationR)-1]-simulateur.dateSimulationR[len(simulateur.dateSimulationR)-simulateur.qr])*simulateur.qr)/(simulateur.nbBusRep - simulateur.qr)

        simulateur.TauxUtilisationCentrereparation = simulateur.histo.aireBr/(2*simulateur.dureeMax)

        simulateur.tailleMoyFileC = simulateur.histo.aireQc/simulateur.dureeMax
        simulateur.tailleMoyFileR = simulateur.histo.aireQr/simulateur.dureeMax
