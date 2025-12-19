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

v1.changerCouleur("rouge")

roues = 0
taille = 0

v1.configurationBase(4, "4m")

print("Couleur :", v1.couleur)
print("Nombre de roues :", v1.nombre_roues)
print("Dimensions :", v1.dimensions)






