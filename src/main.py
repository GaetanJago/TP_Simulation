from src.Simulateur import Simulateur

simulateur = Simulateur(1, 2, 0.3, 120, 65, 15, 270, 126)

tpsAttenteMoyenControle = 0
tpsAttenteMoyenControleSansBusAttente = 0
tpsAttenteMoyenReparation = 0
tpsAttenteMoyenReparationSansBusAttente = 0
tauxUtilisationCentreReparation = 0
tailleMoyFileC = 0
tailleMoyFileR = 0
listeTempsAttenteMaxC = []
listeTempsAttenteMaxR = []


for i in range(500):
    simulateur.resetSimulateur()
    simulateur.lancerAvecDureeMax(240)
    tpsAttenteMoyenControle += simulateur.TpsAttenteMoyControle
    tpsAttenteMoyenReparation += simulateur.TpsAttenteMoyReparation
    tauxUtilisationCentreReparation += simulateur.TauxUtilisationCentrereparation
    tailleMoyFileC += simulateur.tailleMoyFileC
    tailleMoyFileR += simulateur.tailleMoyFileR

    simulateur.calculTempsAttente()
    tempsAttenteMaxC = simulateur.tempsAttenteMaxC()
    tempsAttenteMaxR = simulateur.tempsAttenteMaxR()
    listeTempsAttenteMaxC.append(tempsAttenteMaxC)
    listeTempsAttenteMaxR.append(tempsAttenteMaxR)

print("Temps d'attente moyen avant controle : ", tpsAttenteMoyenControle/500)
print("Temps d'attente moyen avant reparation : ", tpsAttenteMoyenReparation/500)
print("Taux d'utilisation moyen du centre de réparation: ", tauxUtilisationCentreReparation/500)
print("Taille moyenne file controle :", tailleMoyFileC/500)
print("Taille moyenne file reparation :", tailleMoyFileR/500)
print("Temps d'attente maximum des bus dans la file de controle :", max(listeTempsAttenteMaxC))
print("Temps d'attente maximum des bus dans la file de réparation :", max(listeTempsAttenteMaxR))

