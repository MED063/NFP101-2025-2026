#  Conversion décimal vers hexadécimal
# Divisions successives par 16, on garde les restes (0-9, A-F)

def convHexa(n):
    """Convertit un entier positif en hexadécimal (string)"""
    if n == 0:
        return "0"
    hexa_chars = "0123456789ABCDEF"
    hexa = ""
    while n > 0:
        hexa = hexa_chars[n % 16] + hexa 
        n = n // 16  
    return hexa  


print(convHexa(202))  