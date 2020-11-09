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

    def ajouterEvenement(self, heure, evenement):
        iterateur = len(self.echeancier) - 1 # On se positionne a la derniere ligne de l'echeancier
        insere = False
        while insere == False:
            if iterateur == -1:
                self.echeancier.insert(0, (heure, evenement))
                insere = True
            elif self.echeancier[iterateur][0] <= heure:
                self.echeancier.insert(iterateur+1, (heure, evenement))
                insere = True
            iterateur -= 1










