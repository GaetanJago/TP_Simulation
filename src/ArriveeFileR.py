from src.Evenement import Evenement
import src.AccesReparation as AccesReparation
import src.Simulateur as Simulateur

class ArriveeFileR(Evenement):

    def __init__(self):
        super(ArriveeFileR, self).__init__()

    def procedure(self):

        simu = Simulateur.Simulateur()
        simu.qr = simu.qr + 1
        simu.nbBusRep = simu.nbBusRep + 1
        if simu.br < 2 :
            simu.ajouterEvenement(simu.dateSimu, AccesReparation.AccesReparation())

