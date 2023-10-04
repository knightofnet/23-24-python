from random import randint

def saisieSomme() :
    n=int(input("Veuillez saisir un entier"))
    while n < 2 or n > 12 :
        print("Erreur de saisie : n doit etre compris entre 2 et 12")
        n=int(input("Veuillez saisir un entier"))
    return n

def sommeDeuxDes() :
    tirageA = randint(1,6)
    tirageB = randint(1,6)
    somme = tirageA + tirageB
    
    print("dé 1 :", tirageA, " dé 2 :", tirageB)
    print("somme :", somme)
    
    return somme    
    
def jouer() :
    tirageUser = saisieSomme()
    tirageOrdi = sommeDeuxDes()
    
    if tirageOrdi == tirageUser :
        print("Gagné")
    else :
        print("Perdu")

jouer()
