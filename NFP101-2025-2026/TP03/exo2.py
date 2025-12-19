def recherche_min_max(tableau):
    """Recherche la plus petite et la plus grande valeur dans un tableau"""
    if len(tableau) == 0:
        return None, None
    
    minimum = tableau[0]
    maximum = tableau[0]
    
    for valeur in tableau:
        if valeur < minimum:
            minimum = valeur
        if valeur > maximum:
            maximum = valeur
    
    return minimum, maximum


# test
tab = [5, 2, 9, 1, 7, 3, 8]
print(recherche_min_max(tab))  
    
  