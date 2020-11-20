from TP_Simulation.src.Evenement import Evenement
from TP_Simulation.src.Simulateur import Simulateur

class ArriveeFileC(Evenement):

    def __init__(self):
        super(ArriveeFileC, self).__init__()

    def procedure(self):
        simulateur = Simulateur()
        simulateur.qc += 1
        if simulateur.bc == 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle())


