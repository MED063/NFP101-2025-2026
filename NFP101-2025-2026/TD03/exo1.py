def rechSeq(T, val):
    for i, x in enumerate(T):
        if x == val:
            return i
    return -1
#test
print(rechSeq([8, 3, 12, 9, 5, 10, 6], 5))  
