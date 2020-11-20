import  src.AccesControle as AccesControle
from src.Evenement import Evenement

class ArriveeFileC(Evenement):

    def __init__(self):
        super(ArriveeFileC, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        simulateur.qc += 1
        if simulateur.bc == 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesControle.AccesControle())


