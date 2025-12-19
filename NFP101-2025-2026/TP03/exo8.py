# Calcul de la factorielle
# n! = n × (n-1) × (n-2) × ... × 2 × 1

def factoriel(n):
    """Calcule n!"""
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


print(factoriel(4))  