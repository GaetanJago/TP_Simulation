from src.DebutSimulation import DebutSimulation
from src.Singleton import Singleton
from src.Historique import Historique


class Simulateur(metaclass=Singleton):

    # Variables
    nbBus = 0
    qc = 0
    qr = 0
    bc = 0
    br = 0
    nbBusRep = 0

    countFileC = 0
    countFileR = 0

    # Paramètrage du simulateur
    nbPosteControle = None
    nbPosteRep = None
    probaRep = None
    paramLoiArrivee = None
    borneSupControle = None
    borneInfCOntrole = None
    borneSupRep = None
    borneInfRep = None

    listeBusFileR = []
    ListeBusFileC = []

    #Variables de fin de simulation
    TpsAttenteMoyControle = 0
    TpsAttenteMoyReparation = 0
    TauxUtilisationCentrereparation = 0
    tailleMoyFileC = 0
    tailleMoyFileR = 0


    histo = Historique()

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

    def resetSimulateur(self):
        self.dateSimu = 0.0
        self.nbBus = 0
        self.qc = 0
        self.qr = 0
        self.bc = 0
        self.br = 0
        self.nbBusRep = 0

        self.TpsAttenteMoyControle = 0
        self.TpsAttenteMoyReparation = 0
        self.TauxUtilisationCentrereparation = 0
        self.tailleMoyFileC = 0
        self.tailleMoyFileR = 0

        self.histo = Historique()
        self.echeancier = []

        self.dureeMax = 0
        self.nbBusMax = 0


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

            # Mise a jour des aires
            self.miseAJourAires(self.dateSimu, couple[0])

            # maj date
            self.dateSimu = couple[0]
            # Executer evenement
            couple[1].procedure()

            # si la liste n'est pas deja vide
            if len(self.echeancier) > 0:
                # Supprimer de la liste le couple récupéré
                self.echeancier.pop(0)


    def miseAJourAires(self, dateD1, dateD2):
        # print("date D1 :", dateD1)
        # print("date D2 :", dateD2)
        # print(self.histo.aireQc)
        # print(self.qc)
        self.histo.aireQc += (dateD2 - dateD1) * self.qc
        self.histo.aireQr += (dateD2 - dateD1) * self.qr
        self.histo.aireBr += (dateD2 - dateD1) * self.br


    def arriveeBusC(self):
        #bus = [dateentreefileC, dateSortiefileC]
        bus = [self.dateSimu, 0.0]
        self.listeBusFileC.append(bus)

    def sortieBusC(self, numeroBus):
        self.listeBusFileC[numeroBus][1] = self.dateSimu

    def entreeBusR(self):
        #bus =  [dateentreefileR, datesortiefileR]
        bus = [self.dateSimu, 0.0]
        self.listeBusFileR.append(bus)

    def sortieBusR(self, numeroBus):
        self.listeBusFileR[numeroBus][1] = self.dateSimu