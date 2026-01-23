class Personne:
    population = 0   # attribut de classe

    def __init__(self, nom):
        self.nom = nom
        Personne.population += 1

    @classmethod
    def afficher_population(cls):
        print(f"Population : {cls.population}")


p1 = Personne("Med")
p2 = Personne("Amine")

Personne.afficher_population()
