def rechDic(T, val):
    inf, sup = 0, len(T) - 1
    while inf <= sup:
        milieu = (inf + sup) // 2
        if T[milieu] == val:
            return milieu
        elif val > T[milieu]:
            inf = milieu + 1
        else:
            sup = milieu - 1
    return -1
#test
print(rechDic([3, 5, 6, 8, 9, 12, 15, 19, 23, 51], 15))