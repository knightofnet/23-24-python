from math import pi

def saisie():
    n=int(input("Veuillez saisir un entier"))
    while n <= 0  :
        print("Erreur de saisie : n doit etre supérieur à 0")
        n=int(input("Veuillez saisir un entier"))
    return n

def afficherTerme(n) :
    s= 0
    for i in range(1, n + 1) :
        s += 1 / i ** 2
        
    print("Le résultat pour n=", n, "est ", s)
    print("pi ** 2 / 6 :", pi ** 2 / 6)

def main() :
    valeurUtilisateur=saisie()
    afficherTerme(valeurUtilisateur)
main()