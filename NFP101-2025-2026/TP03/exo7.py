# Vérifier si un nombre est premier
# Un nombre premier n'est divisible que par 1 et lui-même

def premier(n):
    """Retourne True si n est premier, False sinon"""
    if n <= 1:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True


print(premier(7))   
print(premier(10))  
  