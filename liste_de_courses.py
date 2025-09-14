import sys
# Construire les choix et l'afficher

Actions = """Choisissez parmi les 5 options suivantes :
1 : Ajouter un élément à la liste
2 : Retirer un élement de la liste
3 : Afficher la liste
4 : Vider la liste
5 : Quitter"""

# Déclarer ma variable

choix_utilisateur = ""


#Créer une liste qui va contenir les éléments choisis par l'utilisateur

MENU_CHOICES = ["1", "2", "3", "4", "5"]

Liste_de_course = []

while True:  # boucle principale du menu
    print(Actions)
    choix_utilisateur = input("👉 Quel est votre choix ? ")

    if choix_utilisateur not in MENU_CHOICES:
        print(f"""{Actions}
⚠️ Veuillez renseigner un chiffre parmi les actions possibles svp 👆""")
        continue # on recommence le menu

    if choix_utilisateur == "1": #Action 1
        ajout_element = input("Entrer le nom de l'élément à ajouter à la liste: ")
        Liste_de_course.append(ajout_element)
        print(f"✅ L'élément {ajout_element} a bien été ajouté à votre liste.")

    elif choix_utilisateur == "2": #Action 2
        supprimer_element = input ("Entrer le nom d'un élément à retirer de la liste: ")
        if supprimer_element in Liste_de_course:
            Liste_de_course.remove(supprimer_element)
            print(f"🗑️ L'élément {supprimer_element} a bien été retiré de votre liste.")
        else:
            print(f"⚠️ L'élément {supprimer_element} n'est pas dans votre liste.")

    elif choix_utilisateur == "3": #Action 3
        if Liste_de_course: #Test si liste vide
            print("🛒 Votre liste de course : ")
            for i, element in enumerate(Liste_de_course, 1):
                print(f"{i}. {element}")
        else:
            print("⚠️ Votre liste est vide.")

    elif choix_utilisateur == "4": #Action 4
        if Liste_de_course:
            Liste_de_course.clear()
            print("✅ Votre liste a été vidée")
        else:
            print("⚠️ Votre liste est déjà vide.")

    elif choix_utilisateur == "5": #Action 5
        print("À bientôt !")
        sys.exit()

    print("-" * 50)




