class Voiture:
    """Initialisation de la doc de la classe Voiture"""
    couleur = "noire"
    marque = "Renault"
    modele = " Clio 4"
    
    def changerCouleur(self, nouvelle_couleur):
        """Change la couleur de la voiture"""
        self.couleur = nouvelle_couleur

    def configurationBase(self, nombre_roues, dimensions):
        """Configure le nombre de roues et les dimensions"""
        self.nombre_roues = nombre_roues
        self.dimensions = dimensions

    def afficherModele(self):
        println(self.couleur)
    