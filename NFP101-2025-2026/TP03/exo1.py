def somme(n):
    """Calcule la somme des n premiers entiers (1 + 2 + ... + n)"""
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


# test
print(f"Somme des 5 premiers entiers : {somme(5)}")
    
