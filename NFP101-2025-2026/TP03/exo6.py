# PPCM de deux entiers
# On cherche le plus petit multiple du max qui soit divisible par le min

def ppcm(a, b):
    """Calcule le PPCM de deux entiers"""
    maximum = max(a, b)
    minimum = min(a, b)
    multiple = maximum
    
    while multiple % minimum != 0:
        multiple += maximum  
    return multiple


print(ppcm(4, 6))    
