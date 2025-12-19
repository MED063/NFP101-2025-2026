# Suite récurrente d'ordre 1
# U0 = 3, Un = 2*Un-1 - 4

def termeSuite(n):
    """Affiche les n premiers termes de la suite"""
    u = 3  # U0
    print(f"U0 = {u}")
    for i in range(1, n):
        u = 2 * u - 4  # relation de récurrence
        print(f"U{i} = {u}")


termeSuite(10)