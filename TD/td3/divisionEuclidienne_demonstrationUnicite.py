import random  # Importe le module random pour générer des nombres aléatoires

def division_euclidienne(a, b):
    """
    Effectue une division euclidienne de 'a' par 'b'.
    
    :param a: Le dividende, un nombre entier.
    :param b: Le diviseur, un nombre entier.
    :return: Un tuple contenant le quotient et le reste de la division.
    """
    q = 0  # Initialise le quotient à 0
    r = a  # Initialise le reste à 'a'
    
    # Boucle tant que le reste est supérieur ou égal à 'b'
    while r >= b:
        q += 1  # Incrémente le quotient
        r -= b  # Diminue le reste par 'b'
    
    return (q, r)  # Retourne le couple (quotient, reste)


def main():
    """
    Fonction principale qui teste la fonction 'division_euclidienne' en 
    générant des valeurs aléatoires pour 'a' et 'b' et en vérifiant si les 
    résultats sont identiques sur des appels répétés.
    
    Permet de tester l'unicité.
    
    :return: None
    """
    n = int(1e5)  # Définit le nombre d'itérations comme 100 000
    
    # Boucle sur 'n' itérations
    for _ in range(n):
        
        # Choisissez des valeurs aléatoires pour a et b
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        
        # Première et deuxième exécution de la division euclidienne
        (q1, r1) = division_euclidienne(a, b)
        (q2, r2) = division_euclidienne(a, b)
        
        # Compare les résultats des deux exécutions et affiche une erreur si 
        # elles ne sont pas identiques
        if (q1, r1) != (q2, r2):
            print("Erreur : Les couples (q, r) ne sont pas identiques pour a =", a, "et b =", b)
            break
    
    print("fin du pgm")  # Affiche un message indiquant la fin du programme


# Exécute la fonction main si ce script est exécuté en tant que script principal
if __name__ == "__main__":
    main()
