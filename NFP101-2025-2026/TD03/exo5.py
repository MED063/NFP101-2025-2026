def triSelection(T):
    for i in range(len(T) - 1):
        min_idx = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_idx]:
                min_idx = j
        T[i], T[min_idx] = T[min_idx], T[i]
    return T

#test

print(triSelection([6, 9, 2, 8, 5, 4]))
