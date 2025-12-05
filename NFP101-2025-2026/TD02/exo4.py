def supprimerElementsNegatifs (listeN):
    return [x for x in listeN if x >= 0]

resultat = supprimerElementsNegatifs([-1, 2, 3, -2])
print(resultat)