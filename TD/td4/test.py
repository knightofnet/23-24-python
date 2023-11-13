def estNegatif(n) :
    if n < 0 :
        return True
    else :
        return False
        
    print("Je ne serais jamais affiché !")


def afficheCalendrier(posLundi):
    # Jours de la semaine
    jours = ["Lu", "Ma", "Me", "Je", "Ve", "Sa", "Di"]

    # Affichage des jours de la semaine
    for jour in jours:
        print(f"{jour} ", end="")
    print()  # Retour à la ligne

    # Affichage des espaces pour le décalage initial
    for i in range(posLundi):
        print("   ", end="")

    # Boucle à travers chaque jour du mois
    jour_du_mois = 1
    for i in range(posLundi, 31 + posLundi):
        print(f"{jour_du_mois:2} ", end="")  # Affichage du jour du mois avec un espace de formatage pour aligner les chiffres à un ou deux chiffres
        jour_du_mois += 1

        if (i + 1) % 7 == 0:  # Retour à la ligne après chaque semaine
            print()

# Test de la fonction
# print("Calendrier avec démarrage le Lundi :")
# afficheCalendrier(0)
# print("\nCalendrier avec démarrage le Dimanche :")
# afficheCalendrier(6)

print(10042 % 1000)
