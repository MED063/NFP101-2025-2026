def triInsertion(T):
    for i in range(1, len(T)):
        cle = T[i]
        j = i - 1
        while j >= 0 and T[j] > cle:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = cle
    return T
#test
print(triInsertion([8, 5, 3, 6, 4, 7]))