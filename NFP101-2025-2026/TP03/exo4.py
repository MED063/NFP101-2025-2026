#  Suite récurrente d'ordre 2
# U0 = 3, U1 = 1, Un = Un-1 + Un-2

def termeSuite2(n):
    """Retourne la valeur de Un"""
    if n == 0:
        return 3
    if n == 1:
        return 1
    
    u_prev2, u_prev1 = 3, 1  # U0, U1
    for i in range(2, n + 1):
        u = u_prev1 + u_prev2  # Relation de récurrence
        u_prev2, u_prev1 = u_prev1, u
    return u


for i in range(10):
    print(f"U{i} = {termeSuite2(i)}")