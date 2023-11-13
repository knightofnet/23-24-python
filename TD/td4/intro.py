def afficheInformations() :

    nom = input("Nom : ")
    afficheTrait('8', 20)

    prenom = input("Prénom : ")
    afficheTrait('_', 3)      

    adresse = input("Adresse : ")
    afficheTrait('+', 100)    

def afficheTrait(car, n) :
    for i in range(1, n + 1) :
        print(car, end='')    
    print()   

afficheInformations()
