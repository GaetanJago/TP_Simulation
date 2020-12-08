from src.Simulateur import Simulateur

simulateur = Simulateur(1, 2, 0.3, 1/2, 13/12, 1/4, 4.5, 2.1)

# dureeMoyenne = 0
tpsAttenteMoyenControle = 0
# tpsAttenteMoyenReparation = 0
# tauxUtilisationCentreReparation = 0
# tailleMoyFileC = 0
# tailleMoyFileR = 0
nbBus = 30
tempsAttenteAvantControleParBus = [0] * nbBus

nbIterations = 500

for i in range(nbIterations):
    simulateur.resetSimulateur()

    # simulateur.lancerAvecDureeMax(240)
    simulateur.lancerAvecNbBusMax(nbBus)

    # dureeMoyenne += simulateur.dateSimu

    for i in range(len(simulateur.histo.tempsAttenteBusAvantControle)):
        tempsAttenteAvantControleParBus[i] += simulateur.histo.tempsAttenteBusAvantControle[i]
    tpsAttenteMoyenControle += simulateur.TpsAttenteMoyControle
    # tpsAttenteMoyenReparation += simulateur.TpsAttenteMoyReparation
    # tauxUtilisationCentreReparation += simulateur.TauxUtilisationCentrereparation
    # tailleMoyFileC += simulateur.tailleMoyFileC
    # tailleMoyFileR += simulateur.tailleMoyFileR

# print("duree moyenne : ", dureeMoyenne/nbIterations)
for i in range(len(simulateur.histo.tempsAttenteBusAvantControle)):
    print("Temps d'attente bus ", i+1, " : ", tempsAttenteAvantControleParBus[i]/nbIterations)

print("Temps d'attente moyen avant controle : ", tpsAttenteMoyenControle/nbIterations)
# print("Temps d'attente moyen avant reparation : ", tpsAttenteMoyenReparation/nbIterations)
# print("Taux d'utilisation moyen du centre de réparation: ", tauxUtilisationCentreReparation/nbIterations)
# print("Taille moyenne file controle :", tailleMoyFileC/nbIterations)
# print("Taille moyenne file reparation :", tailleMoyFileR/nbIterations)

