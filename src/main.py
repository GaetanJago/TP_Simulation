from src.Simulateur import Simulateur

simulateur = Simulateur(1, 2, 0.3, 120, 65, 15, 270, 126)

tpsAttenteMoyenControle = 0
tpsAttenteMoyenReparation = 0
tauxUtilisationCentreReparation = 0


for i in range(500):
    simulateur.resetSimulateur()
    simulateur.lancerAvecDureeMax(240)
    tpsAttenteMoyenControle += simulateur.TpsAttenteMoyControle
    tpsAttenteMoyenReparation += simulateur.TpsAttenteMoyReparation
    tauxUtilisationCentreReparation += simulateur.TauxUtilisationCentrereparation

print("Temps d'attente moyen avant controle : ", tpsAttenteMoyenControle/500)
print("Temps d'attente moyen avant reparation : ", tpsAttenteMoyenReparation/500)
print("Taux d'utilisation moyen du centre de réparation: ", tauxUtilisationCentreReparation/500)

