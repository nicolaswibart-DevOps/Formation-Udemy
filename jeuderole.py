import random 

# Déclarer les variables
health_user = 50
health_enemy = 50

number_of_potion = 3


choices = ["1","2"]


#Boucle principale
while health_user > 0 and health_enemy > 0:
    choice_user = input("Souhaitez-vous attaquer (1) ou prendre une potion (2) ? ")
    
    if choice_user not in choices: #Faire en sorte que l'utilisateur rentre une commande valide
        print("⚠️ Veuillez renseigner un choix valide : (1) attaquer ou (2) prendre une potion")
        continue

    attack_user = random.randint(5, 10)
    attack_enemy = random.randint(5, 15)

    if choice_user == "1": #Action 1
        
        health_enemy = (health_enemy - attack_user)
        print(f"Vous avez infligé {attack_user} points de dégât1s à l'ennemie ⚔️")
        if health_enemy <= 0:
            break
        health_user = (health_user - attack_enemy)
        print(f"L'ennemi vous a infligé {attack_enemy} points de dégâts ⚔️")
        print(f"Il vous reste {health_user} points de vie.")
        print(f"Il reste {health_enemy} points de vie à l'ennemie")

    elif choice_user == "2": #Action 2
        if number_of_potion > 0: #Limiter le nb de potions
            heal_potion = random.randint (15, 51)
            health_user = health_user + heal_potion
            health_user = (health_user - attack_enemy)
            number_of_potion -= 1
            print(f"Vous avez récupéré {heal_potion} points de vie ❤️ ({number_of_potion} 🧪 restantes) ⚔️")
            print(f"L'ennemi vous a infligé {attack_enemy} points de dégâts ⚔️")
            print(f"Il vous reste {health_user} points de vie.")
            print(f"Il reste {health_enemy} points de vie à l'ennemie")
            print("-" * 100)

            # Passe tour
            print("Vous passez votre tour...") 
            health_user = (health_user - attack_enemy)
            print(f"L'ennemi vous attaque de nouveau {attack_enemy} points de dégâts ⚔️")
            print(f"Il vous reste {health_user} points de vie.")
            print(f"Il reste {health_enemy} points de vie à l'ennemie")
        else:
            print("🚨 Il ne vous reste plus de potion")
    print("-" * 100)

# Cas ou on gagne ou on perd
if health_user <= 0:
    print("GAME OVER ❌")
if health_enemy <= 0:
    print("SUCCED 💪")

print("Fin du jeu")
