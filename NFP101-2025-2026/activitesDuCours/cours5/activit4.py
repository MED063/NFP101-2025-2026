class Voiture:
    """Initialisation de la doc de la classe Voiture"""
    couleur = "noire"
    marque = "Renault"
    
    def changerCouleur(self, nouvelle_couleur):
        """Change la couleur de la voiture"""
        self.couleur = nouvelle_couleur
    
    def configurationBase(self, nombre_roues, dimensions):
        """Configure le nombre de roues et les dimensions"""
        self.nombre_roues = nombre_roues
        self.dimensions = dimensions


v1 = Voiture()
print(v1.couleur)  

v1.changerCouleur("blanche")
print(v1.couleur)  

v1.configurationBase(4, "4m x 2m x 1.5m")
print(v1.nombre_roues) 
print(v1.dimensions) 