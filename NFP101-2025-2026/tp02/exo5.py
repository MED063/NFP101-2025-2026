def compter_z(chaine):
    liste_caracteres = list(chaine)
    
    compteur = 0
    for caractere in liste_caracteres:
        if caractere == 'z':
            compteur += 1
    return compteur


texte='zoozo zooz'
print(f"Nombre de 'z' dans '{texte}' : {compter_z(texte)}")