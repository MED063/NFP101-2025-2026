def nb_billes_pyramide(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i  
    return total
 
etages = int(input("entrez le nb d'etages : "))

print(f"nombre total de billes pour une pyramide de {etages} etages  :  {nb_billes_pyramide(etages)}")
