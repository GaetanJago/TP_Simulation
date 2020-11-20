from src.AccesReparation import AccesReparation
from src.Evenement import Evenement
from src.Maths import *
from src.Simulateur import Simulateur


class DepartReparation (Evenement):


    def __init__(self):
        pass

    def procedure(self):
        simulateur = Simulateur()
        # on libère un poste dans le centre de réparation
        simulateur.br = simulateur.br - 1
        #on ajoute un evenement accesReparation dans l'echéancier si la file R n'est pas vide
        if simulateur.qr > 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesReparation())