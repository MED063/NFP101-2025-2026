def afficheDiviseur(n):
    if n < 1:
        print("entrez un nombre sup a 1")
        return

    diviseurs = []
    for i in range(1, n + 1):
        if n % i == 0:
            diviseurs.append(i)
    
    if len(diviseurs) == 2:  
        print(f"Diviseurs de {n} : aucun diviseur")
    else:
        print(f"Diviseurs de {n} : {diviseurs}")

afficheDiviseur(12)
afficheDiviseur(13)
