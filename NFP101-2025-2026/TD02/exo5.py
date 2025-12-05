import random

def demander_limites():
    
    while True:
        try:
            min_val = int(input("Borne minimale : "))
            max_val = int(input("Borne maximale : "))
            if min_val < max_val:
                return min_val, max_val
            print("Erreur : min doit être < max")
        except ValueError:
            print("Entrez des nombres entiers")

def tirer_nombre_myster(min_val, max_val):
   
    return random.randint(min_val, max_val)

def demander_proposition(min_val, max_val):
    
    while True:
        try:
            prop = int(input(f"Nombre entre {min_val} et {max_val} : "))
            if min_val <= prop <= max_val:
                return prop
            print(f"Le nombre doit être entre {min_val} et {max_val}")
        except ValueError:
            print("Entrez un nombre entier")

def analyser_propo(proposition, secret):
    
    if proposition < secret:
        return -1
    elif proposition > secret:
        return 1
    else:
        return 0

def jouer_une_partie():
    
    print("\nNouvelle partie")
    min_val, max_val = demander_limites()
    secret = tirer_nombre_myster(min_val, max_val)
    tentatives = 0

    while True:
        tentatives += 1
        proposition = demander_proposition(min_val, max_val)
        resultat = analyser_propo(proposition, secret)

        if resultat == -1:
            print("Trop petit")
        elif resultat == 1:
            print("Trop grand")
        else:
            print(f"Trouvé en {tentatives} tentative(s)")
            return

def demander_rejouer():
    
    while True:
        reponse = input("Rejouer ? (o/n) : ").lower().strip()
        if reponse in ('o', 'oui'):
            return True
        elif reponse in ('n', 'non'):
            return False
        else:
            print("Réponse invalide")

# Programme principal
if __name__ == "__main__":
    print("Bienvenue dans le jeu du nbr Mystere")

    while True:
        jouer_une_partie()
        if not demander_rejouer():
            print("Au revoir")
            break
