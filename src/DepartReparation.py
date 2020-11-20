import src.AccesReparation as AccesReparation
from src.Evenement import Evenement


class DepartReparation (Evenement):

    def __init__(self):
        super(DepartReparation, self).__init__()

    def procedure(self):
        from src.Simulateur import Simulateur
        simulateur = Simulateur()
        # on libère un poste dans le centre de réparation
        simulateur.br = simulateur.br - 1
        #on ajoute un evenement accesReparation dans l'echéancier si la file R n'est pas vide
        if simulateur.qr > 0:
            simulateur.ajouterEvenement(simulateur.dateSimu, AccesReparation.AccesReparation())