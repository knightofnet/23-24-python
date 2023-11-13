from math import e

def factoriel(n):
    resu = 1
    for i in range(1,n+1) :
        resu=resu*i
    return resu

def somme(n):
    s = 0
    for i in range(0, n + 1) :
        s += 1/ factoriel(i)
    return s

def estimation(delta) :
    n = 1
    eApproche = somme(n)
    
    while abs(e - eApproche) > delta  :
        n = n + 1
        eApproche = somme(n)
        
    return n

assert estimation(0.0001) == 7

print(estimation(0.0001))




