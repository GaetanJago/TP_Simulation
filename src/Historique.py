import matplotlib.pyplot as plt
import numpy as np

class Historique:
    aireQc = 0
    aireQr = 0
    aireBr = 0

    def __init__(self, nbBusHisto, qcHisto, qrHisto, bcHisto, nbBusRepHisto, brHisto):
        self.nbBusHisto = nbBusHisto
        self.qcHisto = qcHisto  # nombre de bus dans la file C
        self.qrHisto = qrHisto  # nombre de bus dans la file R
        self.bcHisto = bcHisto  # le statut centre de controle
        self.nbBusRepHisto = nbBusRepHisto  # nombre de bus repares
        self.brHisto = brHisto # le statut centre de reparation

    def afficherGraphe(self):
        print("afficher graphe")

        plt.plot(np.array(range(len(self.nbBusHisto))), self.nbBusHisto, marker='o', label='nbBusHisto')
        plt.plot(np.array(range(len(self.qcHisto))), self.qcHisto, marker='*', label='qcHisto')
        plt.plot(np.array(range(len(self.qrHisto))), self.qrHisto, marker='v', label='qrHisto')
        plt.plot(np.array(range(len(self.bcHisto))), self.bcHisto, marker='.', label='bcHisto')
        plt.plot(np.array(range(len(self.nbBusRepHisto))), self.nbBusRepHisto, marker='s', label='nbBusRepHisto')
        plt.plot(np.array(range(len(self.brHisto))), self.brHisto, marker='>', label='nbBusRepHisto')
        plt.legend()

        plt.margins(0)
        plt.title('Graphe d\'historique')
        plt.xlabel('Historique')
        plt.ylabel("Nombre")

        plt.show()

    def calcAire(self, D1, D2):
        print("calculer des aires")
        self.aireQc, self.aireQr, self.aireBr = 0, 0, 0
        for qc in self.qcHisto:
            self.aireQc += (D2 - D1)*qc
        for qr in self.qrHisto:
            self.aireQr += (D2 - D1)*qr
        for br in self.brHisto:
            self.aireBr += (D2 - D1)*br
        print(self.aireQc, self.aireQr, self.aireBr)
        return self.aireQc, self.aireQr, self.aireBr

    def attenteMoy(self, nbBus, nbBusRep, D1, D2):
        print("calculer le temps d'attente moyen")
        aireQc, aireQr, aireBr = self.calcAire(D1, D2)
        tempsMoyAvantC = aireQc/nbBus
        tempsMoyAvantR = aireQr/nbBusRep
        tauxUtilisation = aireBr/(2*160)
        print(tempsMoyAvantC, tempsMoyAvantR, tauxUtilisation)
        return tempsMoyAvantC, tempsMoyAvantR, tauxUtilisation

    def attenteMoyTotal(self, nbBus, nbBusRep, D1, D2):
        print("calculer le temps d'attente moyen totale")
        tempsMoyAvantC, tempsMoyAvantR, tauxUtilisation = self.attenteMoy(nbBus, nbBusRep, D1, D2)
        tempsMoyTotal = tempsMoyAvantC + tempsMoyAvantR
        print(tempsMoyTotal)
        return tempsMoyTotal


if __name__ == '__main__':
    histo = Historique([1,3,4], [23, 4, 5, 6], [9, 7, 2], [10, 5, 8, 7, 6], [4, 6, 3], [1, 0, 1])
    # Historique.afficherGraphe(histo)
    Historique.calcAire(histo, 1, 11)
    Historique.attenteMoy(histo, 10, 5, 1, 11)
    Historique.attenteMoyTotal(histo, 10, 5, 1, 11)