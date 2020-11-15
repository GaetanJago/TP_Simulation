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


    #TODO Ajouter historique
    minuteActuelle = 0.0
    echeancier = []

    compteurEvenement = 0

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

    def ajouterEvenement(self, minute, evenement):
        iterateur = len(self.echeancier) - 1 # On se positionne a la derniere ligne de l'echeancier
        insere = False
        while insere == False:
            if iterateur == -1:
                self.echeancier.insert(0, (minute, evenement))
                insere = True
            elif self.echeancier[iterateur][0] <= minute:
                self.echeancier.insert(iterateur+1, (minute, evenement))
                insere = True
            iterateur -= 1

    def lancerAvecDureeMax(self, duree):
        self.minuteActuelle = 480

        # Ajout de l'evenement de debut de simulation
        self.ajouterEvenement(self.minuteActuelle, DebutSimulation())

        # Ajout de l'evt de fin de simulation
        self.ajouterEvenement(self.minuteActuelle + duree, FinSimulation())

        while self.compteurEvenement < len(self.echeancier):
            evenement = self.echeancier[self.compteurEvenement]
            #TODO ajouter historique calcAire
            self.minuteActuelle = evenement[0]

            # Executer evenement
            evenement[1].procedure()
            self.compteurEvenement += 1



