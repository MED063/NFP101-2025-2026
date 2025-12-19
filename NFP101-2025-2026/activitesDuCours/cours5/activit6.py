class Voiture:
    """Initialisation de la doc de la classe Voiture"""
    
    #init 
    couleur = 0
    roues = 0
    taille = 0
    marque = "Renault"
    
    def changerCouleur(self, nouvelle_couleur):
        """Change la couleur de la voiture"""
        self.couleur = nouvelle_couleur
    
    def configurationBase(self, roues=4, taille=200):
        """Configure le nombre de roues et la taille"""
        self.roues = roues
        self.taille = taille
        
        
        print("Couleur :", self.couleur)
        print("Roues :", self.roues)
        print("Taille :", self.taille)



v1 = Voiture()

v1.changerCouleur("blanche")

v1.configurationBase()
