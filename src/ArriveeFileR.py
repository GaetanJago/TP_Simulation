from Evenement import Evenement
import  AccesReparation as AccesReparation

class ArriveeFileR(Evenement):

    def __init__(self):
        super(ArriveeFileR, self).__init__()

    def procedure(self):
        from Simulateur import Simulateur
        simu = Simulateur()
        simu.qr = simu.qr + 1
        simu.nbBusRep = simu.nbBusRep + 1
        if simu.br < 2 :
            simu.ajouterEvenement(simu.dateSimu, AccesReparation.AccesReparation())

