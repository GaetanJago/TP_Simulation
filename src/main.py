from src.Simulateur import Simulateur
import matplotlib.pyplot as plt

def question4():

    # LECTURE DES DONNEES
    with open('DonneesControle.txt') as f:
        dateArr = []
        dureeInter = []
        tmpCont = []

        prec = 0
        nbBus = 0
        for line in f:
            nbBus += 1
            f_list = [float(i) for i in line.split()]
            dureeInter.append(float(f_list[0]) - prec)
            prec = float(f_list[0])
            dateArr.append(float(f_list[0]))
            tmpCont.append(float(f_list[1]))

    # EXPO
    print('============== EXPO ==============')
    print('''Temps d'inter-arrivé moyen (esperance) : ''', sum(dureeInter) / nbBus, ' (Recherché : 2)')

    # UNIFORME
    print('============== UNI ==============')
    a = min(tmpCont)
    b = max(tmpCont)
    print('''Borne minimale de la loi uniforme : ''', a, " (Recherché : 0.25)")
    print('''Borne maximale de la loi uniforme : ''', b, " (Recherché : 1.0833)")
    print('''Esperance selon les bornes''', (a+b) / 2, " (Recherché : 0.6666)")
    print('''Durée de controle moyenne : ''' , sum(tmpCont)/len(tmpCont))

    # COURBES
    plt.subplot(1, 2, 1)
    plt.title('''Loi d'inter-arrivée''')
    x = range(0,nbBus)
    n, bins, patches = plt.hist(dureeInter, 20, facecolor='c', alpha=0.5)

    plt.subplot(1, 2, 2)
    plt.title('''Loi de durée de contrôle''')
    x = range(0, nbBus)
    n, bins, patches = plt.hist(tmpCont, 40, facecolor='c', alpha=0.5)

    plt.show()


def simulator():
    nbSimu = 500

    simulateur = Simulateur(1, 2, 0.3, 120, 65, 15, 270, 126)

    tpsAttenteMoyenControle = 0
    tpsAttenteMoyenReparation = 0
    tauxUtilisationCentreReparation = 0
    tailleMoyFileC = 0
    tailleMoyFileR = 0


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

# Launch question 4
question4()

# Launch simulateur
# simulator()