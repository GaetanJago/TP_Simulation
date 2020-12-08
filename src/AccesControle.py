from src.Evenement import Evenement
from src.Maths import *
import src.DepartControle as DepartControle
import src.FinSimulation as FinSimulation
import src.Simulateur as Simulateur

class AccesControle(Evenement):

    def __init__(self):
        super(AccesControle, self).__init__()

    def procedure(self):

        simulateur = Simulateur.Simulateur()
        simulateur.qc -= 1
        simulateur.bc = 1

        simulateur.histo.datesBusAccesControle.append(simulateur.dateSimu)

        # Si le nombre de bus max est > 0
        # Et que le nombre de bus etant entre dans le poste de controle est egal au nombre de bus max
        if simulateur.nbBusMax > 0 and simulateur.nbBus-simulateur.qc == simulateur.nbBusMax:
            simulateur.ajouterEvenement(simulateur.dateSimu, FinSimulation.FinSimulation())

        simulateur.ajouterEvenement(simulateur.dateSimu + uniforme(1/4,13/12), DepartControle.DepartControle())
