from TP_Simulation.src.Singleton import Singleton

class Simulateur(metaclass=Singleton):

    # Variables
    nbBus = 0
    qc = 0
    qr = 0
    bc = 0
    br = 0
    nbBusRep = 0

    # Paramètrage du simulateur
    nbPosteControle = None
    nbPosteRep = None
    probaRep = None
    paramLoiArrivee = None
    borneSupControle = None
    borneInfCOntrole = None
    borneSupRep = None
    borneInfRep = None


    #TODO Ajouter historique
    heureActuelle = 0.0
    echeancier = []

    def __init__(self):
        pass

    def __init__(self, nbPosteControle, nbPosteRep, probaRep, paramLoiArrive, borneSupControle, borneInfControle, borneSupRep, borneInfRep):
        self.nbPosteControle = nbPosteControle
        self.nbPosteRep = nbPosteRep
        self.probaRep = probaRep
        self.paramLoiArrive = paramLoiArrive
        self.borneSupControle = borneSupControle
        self.borneInfControle = borneInfControle
        self.borneSupRep = borneSupRep
        self.borneInfRep = borneInfRep







