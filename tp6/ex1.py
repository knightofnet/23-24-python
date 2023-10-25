from time import time

def q1() :
    for m in range(5,25) :
        debut = time()
        print(sum([n ** 2 for n in range(2 ** m)]))
        print(m, ":",time() - debut)

def q1B() :
    precDuree = 0
    for m in range(5,25) :
        debut = time()
        print(sum([n ** 2 for n in range(2 ** m)]))
        duree = time() - debut
        print(m, ":",duree)    
        if (precDuree > 0 and duree > 0) :
            print(" x", duree / precDuree )
        precDuree = duree
    

    
def tri_bulle(liste_entree):
    liste = liste_entree
    n = len(liste)
    for j in range(1, n):
        for i in range(n - j):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
    return liste

from random import randint

def q2() :
    for m in range(1,25) :        
        liste = [ randint(-1000,1000) for _ in range(2 **m) ]
        debut = time()        
        tri_bulle(liste)
        print(m, ":",time() - debut)

q2()