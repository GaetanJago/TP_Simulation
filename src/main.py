from Simulateur import Simulateur

simulateur = Simulateur(1, 2, 0.3, 120, 65, 15, 270, 126)

tpsAttenteMoyenControle = 0
tpsAttenteMoyenReparation = 0
tauxUtilisationCentreReparation = 0
tailleMoyFileC = 0
tailleMoyFileR = 0

tpsAttenteMoyenControleExcluentBusAttente = 0
tpsAttenteMoyenReparationExcluentBusAttente = 0
tpsAttenteMaximalAvantControle = []
tpsAttenteMaximalAvantReparation = []

nbSimu = 500

for i in range(nbSimu):
    simulateur.resetSimulateur()
    simulateur.lancerAvecDureeMax(160)
    tpsAttenteMoyenControle += simulateur.TpsAttenteMoyControle
    tpsAttenteMoyenReparation += simulateur.TpsAttenteMoyReparation
    tauxUtilisationCentreReparation += simulateur.TauxUtilisationCentrereparation
    tailleMoyFileC += simulateur.tailleMoyFileC
    tailleMoyFileR += simulateur.tailleMoyFileR

    tpsAttenteMoyenControleExcluentBusAttente += simulateur.TpsAttenteMoyenControleExcluentBusAttente
    tpsAttenteMoyenReparationExcluentBusAttente += simulateur.TpsAttenteMoyenReparationExcluentBusAttente

for i in range(len(simulateur.dateSimulationC)-1):
    tpsAttenteMaximalAvantControle.append(simulateur.dateSimulationC[i+1] - simulateur.dateSimulationC[i])

for i in range(len(simulateur.dateSimulationR)-1):
    tpsAttenteMaximalAvantReparation.append(simulateur.dateSimulationR[i+1] - simulateur.dateSimulationR[i])

print("Temps d'attente moyen avant controle : ", tpsAttenteMoyenControle/nbSimu)
print("Temps d'attente moyen avant reparation : ", tpsAttenteMoyenReparation/nbSimu)
print("Taux d'utilisation moyen du centre de réparation: ", tauxUtilisationCentreReparation/nbSimu)
print("Taille moyenne file controle :", tailleMoyFileC/nbSimu)
print("Taille moyenne file reparation :", tailleMoyFileR/nbSimu)

print("Temps d'attente moyen avant controle excluant les bus d'attente: ", tpsAttenteMoyenControleExcluentBusAttente/nbSimu)
print("Temps d'attente moyen avant reparation excluant les bus d'attente: ", tpsAttenteMoyenReparationExcluentBusAttente/nbSimu)
print("Temps maximal avant controle: ", max(tpsAttenteMaximalAvantControle))
print("Temps maximal avant reparation: ", max(tpsAttenteMaximalAvantReparation))