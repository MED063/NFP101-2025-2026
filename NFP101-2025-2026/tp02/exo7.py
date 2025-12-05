import random

def generer_question():
    a = random.randint(1, 9)
    b = random.randint(10, 89)
    operation = random.choice(["+", "-", "*"])
    
    if operation == "+":
        question = f"{a} + {b} = ?"
        reponse = a + b
    elif operation == "-":
        question = f"{a} - {b} = ?"
        reponse = a - b
    else:  
        question = f"{a} * {b} = ?"
        reponse = a * b
    
    return question, reponse

def lancer_quiz(nb_questions):
    bonnes_reponses = 0
    i = 1
    
    while i <= nb_questions:
        question, reponse_correcte = generer_question()
        print(f"\nQuestion {i} : {question}")
        
        while True:
            try:
                user_input = int(input("Votre réponse : "))
                break
            except ValueError:
                print(" entrer un nombre entier")
        
        if user_input == reponse_correcte:
            print("Correct !")
            bonnes_reponses += 1
        else:
            print(f"faux, la bonne réponse était {reponse_correcte}")
        
        i += 1
    
    score = bonnes_reponses / nb_questions * 100
    print(f"\nVous avez {bonnes_reponses} bonnes réponses sur {nb_questions}.")
    print(f"Votre score est : {score:.2f}%")
    
    if score > 80:
        print("Bravo !")
    elif score >= 50:
        print("Pas mal, entraine toi")
    else:
        print("il faut reviser encore")
    
    return score

def menu_quiz():
    meilleur_score = 0
    
    while True:
        print("\n$ MENU ")
        print("1. faire le quiz")
        print("2. Meilleur score")
        print("3. Quitter")
        choix = input("Votre choix : ")
        
        if choix == "1":
            while True:
                try:
                    nb_questions = int(input("Combien de questions ? "))
                    if nb_questions > 0:
                        break
                    else:
                        print("minimum une question")
                except ValueError:
                    print("Veuillez entrer un nombre entier")
            
            score = lancer_quiz(nb_questions)
            if score > meilleur_score:
                meilleur_score = score
        elif choix == "2":
            print(f"Meilleur score : {meilleur_score}%")
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

menu_quiz()