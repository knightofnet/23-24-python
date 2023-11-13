def afficheInformations() :

    nom = input("Nom : ")
    afficheTrait()        

    prenom = input("Prénom : ")
    afficheTrait()        

    adresse = input("Adresse : ")
    afficheTrait()        

def afficheTrait() :
    for i in range(1, 20 + 1) :
        print('_', end='')  
    print()    

afficheInformations()