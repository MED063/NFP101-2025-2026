def sommeChoix(n):
    """Calcule la somme de n entiers saisis par l'utilisateur"""
    s = 0
    for i in range(n):
        valeur = int(input(f"Entrez l'entier {i + 1} : "))
        s += valeur
    print(f"La somme des {n} entiers est : {s}")
    return s

# test
print("\n=== Test de sommeChoix ===")
sommeChoix(3)