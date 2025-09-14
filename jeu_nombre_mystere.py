import random

nombre_mystere = random.randint(1, 100)
essai = 5

choices = list(range(1,101))



while essai > 0:
    print(f""" ⁇ Bienvenu dans le jeu du nombre Mystère ⁇
il vous reste {essai} essais""")
    utilisateur_choice = input("Devine le nombre (entre 1 et 100) : ")

    if not utilisateur_choice.isdigit():
        print(("⚠️ Veuillez entrer un chiffre"))
        continue

    utilisateur_choice = int(utilisateur_choice)

    if utilisateur_choice not in choices:
        print("⚠️ Veuillez entrer un chiffre en 1 à 100")
        continue
    
    essai -= 1

    if utilisateur_choice < nombre_mystere:#cas où valeur plus grande
        print(f"Le nombre mystère est plus grand que {utilisateur_choice}") 
    elif utilisateur_choice > nombre_mystere:#cas où valeur est plus petite
        print(f"Le nombre mystère est plus petit que {utilisateur_choice}")
    else:
        print(f"""Bravo ! Le nombre mystère était bien {utilisateur_choice}
        Tu as trouvé en {5 - essai} essais""")
        break
else: #cas où le joueur ne trouve pas
    print(f"""Domage le nombre mystère était {nombre_mystere}
    Fin du jeu.""")

