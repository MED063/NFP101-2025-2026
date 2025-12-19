def triBulles(T):
    n = len(T)
    for i in range(n - 1):
        permut = False
        for j in range(n - 1 - i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                permut = True
        if not permut:
            break
    return T
#test

print(triBulles([7, 3, 18, 5, 13]))