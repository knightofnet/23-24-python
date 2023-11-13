def afficheSommeCarre(n) :
    somme = 0;
    for i in range(1, n+1) :
        somme += i ** 2
    print("Somme des carrés de 1 à {} = {}".format(n, somme))

"""
while True : 
    try :
        nSaisi = int(input("Entrez un entier n>= 0 : "))
        if nSaisi < 0 :
            raise ValueError        
        afficheSommeCarre(nSaisi)    
    except ValueError as msg :
        print("Pb de saisie !")
    else :
        break
"""
"""
def saisit() :
    while True : 
        try :
            nSaisi = int(input("Entrez un entier n>= 0 : "))
            if nSaisi < 0 :
                raise ValueError        

            return nSaisi
            
        except ValueError as msg :
            print("Pb de saisie !")

nBis = saisit()
afficheSommeCarre(nBis) 
"""

def estEntierPositif(s) :
    for car in s :
        if car < "0" or car > "9" :
            return False
        
    return True

def saisit2() :
    sSaisi = input("Entrez un entier n>= 0 : ")

    while not(estEntierPositif(sSaisi)) :
        
        print("Pb de saisie")
        sSaisi = input("Entrez un entier n>= 0 : ")

    return int(sSaisi)


nBis = saisit2()
afficheSommeCarre(nBis) 
