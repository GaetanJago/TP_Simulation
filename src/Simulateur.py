from src.DebutSimulation import DebutSimulation
from src.Evenement import Evenement
from src.FinSimulation import FinSimulation
from src.Singleton import Singleton

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

    dureeMax = 0
    nbBusMax = 0

    #TODO Ajouter historique

    dateSimu = 0.0
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

    def ajouterEvenement(self, date, evenement):
        iterateur = len(self.echeancier) - 1 # On se positionne a la derniere ligne de l'echeancier
        insere = False
        while insere == False:
            if iterateur == -1:
                self.echeancier.insert(0, (date, evenement))
                insere = True
            elif self.echeancier[iterateur][0] <= date:
                self.echeancier.insert(iterateur+1, (date, evenement))
                insere = True
            iterateur -= 1

    def lancerAvecDureeMax(self, dureeMax):
        self.dureeMax = dureeMax

        self.dateSimu = 0

        # TODO MaJ historique (init)

        self.ajouterEvenement(self.dateSimu, DebutSimulation())

        while len(self.echeancier) != 0:
            # Récupérer le premier couple de l'échéancier
            couple = self.echeancier[0]

            # Supprimer de la liste le couple récupéré
            self.echeancier = self.echeancier[1:]

            # maj date
            self.dateSimu = couple[0]
            # Executer evenement
            couple[1].procedure()

            # TODO MaJ historique



