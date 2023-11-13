def afficheInformations() :

    nom = input("Nom : ")
    afficheTrait('_', 20)        

    prenom = input("Prénom : ")
    afficheTrait('*', 5)        

    adresse = input("Adresse : ")
    afficheTrait('-', 10)        

def afficheTrait(car, n) :
    for i in range(1, n + 1) :
        print(car, end='')  
    print()    

afficheInformations()