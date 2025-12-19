# PGCD par la méthode d'Euclide
# PGCD(a, b) = PGCD(b, r) où r = a mod b

def pgcd(a, b):
    """Calcule le PGCD de deux entiers"""
    while b != 0:
        r = a % b  
        a = b
        b = r
    return a


print(pgcd(48, 18))   
