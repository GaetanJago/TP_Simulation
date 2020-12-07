import AccesControle as AccesControle
from Evenement import Evenement

class ArriveeFileC(Evenement):

    def __init__(self):
        super(ArriveeFileC, self).__init__()

    def procedure(self):
        from Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.qc += 1
        if simulateur.bc == 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle.AccesControle())


