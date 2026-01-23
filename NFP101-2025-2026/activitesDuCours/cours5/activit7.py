class Voiture:
    def __init__(self, marque, modele, vitesse_max):
        self.marque = marque              # PUBLIC
        self._modele = modele              # PROTÉGÉ
        self.__vitesse_max = vitesse_max   # PRIVÉ

    # Getters
    def get_modele(self):
        return self._modele

    def get_vitesse_max(self):
        return self.__vitesse_max

    # Setters
    def set_modele(self, modele):
        self._modele = modele

    def set_vitesse_max(self, vitesse):
        if vitesse > 0:
            self.__vitesse_max = vitesse

    def demarrer(self):                    # PUBLIC
        print(f"{self.marque} démarre")
        self.__verifier_moteur()

    def _calculer_consommation(self, km):  # PROTÉGÉ
        return km * 0.05

    def __verifier_moteur(self):           # PRIVÉ
        print(f"Moteur OK - Vmax: {self.__vitesse_max} km/h")


# Tests d'accès
v1 = Voiture("Renault", "Clio", 180)

print("Attributs : ")
print(f"PUBLIC: {v1.marque}")
print(f"PROTÉGÉ: {v1._modele}")
try:
    print(v1.__vitesse_max)
except AttributeError:
    print(f"PRIVÉ: Erreur - Accessible via {v1._Voiture__vitesse_max}")

print("\n Méthodes :")
v1.demarrer()  # Appelle aussi __verifier_moteur()
print(f"Consommation: {v1._calculer_consommation(100)}L")
