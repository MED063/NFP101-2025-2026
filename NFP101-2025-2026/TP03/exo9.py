# Conversion décimal vers binaire
# Divisions successives par 2, on garde les restes

def convBinaire(n):
    """Convertit un entier positif en binaire (string)"""
    if n == 0:
        return "0"
    binaire = ""
    while n > 0:
        binaire = str(n % 2) + binaire  # 
        n = n // 2  
    return binaire


print(convBinaire(14))   