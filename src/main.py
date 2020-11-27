from src.Simulateur import Simulateur

simulateur = Simulateur(1, 2, 0.3, 120, 65, 15, 270, 126)

tpsAttenteMoyenControle = 0
tpsAttenteMoyenReparation = 0
tauxUtilisationCentreReparation = 0
tailleMoyFileC = 0
tailleMoyFileR = 0

nbSimu = 500

for i in range(nbSimu):
    simulateur.resetSimulateur()
    simulateur.lancerAvecDureeMax(240)
    tpsAttenteMoyenControle += simulateur.TpsAttenteMoyControle
    tpsAttenteMoyenReparation += simulateur.TpsAttenteMoyReparation
    tauxUtilisationCentreReparation += simulateur.TauxUtilisationCentrereparation
    tailleMoyFileC += simulateur.tailleMoyFileC
    tailleMoyFileR += simulateur.tailleMoyFileR

print("Temps d'attente moyen avant controle : ", tpsAttenteMoyenControle/nbSimu)
print("Temps d'attente moyen avant reparation : ", tpsAttenteMoyenReparation/nbSimu)
print("Taux d'utilisation moyen du centre de réparation: ", tauxUtilisationCentreReparation/nbSimu)
print("Taille moyenne file controle :", tailleMoyFileC/nbSimu)
print("Taille moyenne file reparation :", tailleMoyFileR/nbSimu)

