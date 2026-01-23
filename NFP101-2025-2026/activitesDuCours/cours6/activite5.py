class Voiture:
    def __init__(self, marque, modele, vitesse_max):
        self.marque = marque              # PUBLIC
        self._modele = modele              # PROTÉGÉ
        self.__vitesse_max = vitesse_max   # PRIVÉ

    # ---------- PROPERTIES ----------

    @property
    def modele(self):
        # GETTER
        return self._modele

    @modele.setter
    def modele(self, modele):
        # SETTER
        self._modele = modele

    @property
    def vitesse_max(self):
        # GETTER
        return self.__vitesse_max

    

    # ---------- MÉTHODES ----------

    def demarrer(self):                    # PUBLIC
        print(f"{self.marque} démarre")
        self.__verifier_moteur()

    def _calculer_consommation(self, km):  # PROTÉGÉ
        return km * 0.05

    def __verifier_moteur(self):           # PRIVÉ
        print(f"Moteur OK - Vmax: {self.__vitesse_max} km/h")


# ---------- TESTS ----------
v1 = Voiture("Renault", "Clio", 180)

print("Attributs")
print(f"PUBLIC: {v1.marque}")

# Utilisation des properties
print(f"MODELE (property): {v1.modele}")
v1.modele = "Clio RS"


print("\nMéthodes")
v1.demarrer()
print(f"Consommation: {v1._calculer_consommation(100)} L")
