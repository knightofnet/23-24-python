def fonction1(x,n):
    p=1
    liste=[p]
    for i in range(1,n+1):
        p=p*x
        liste.append(p)
    return liste

def fonction2(liste,x,n):
    if len(liste)>= n+1 :
        return liste[:n+1]
    else:
        p=liste[len(liste)-1]
        for i in range(len(liste),n+1):
            p=p*x
            liste.append(p)
        return liste

from time import time

def evalFn1(N) :
    start_time = time()
    for _ in range(N) :        
        fonction1(2,10)
        fonction1(2,5)
        fonction1(2,12)
    duration = time() - start_time
    print("FN1 :",N, "Durée : ", duration)

def evalFn2(N) :
    start_time = time()
    for _ in range(N) :
        maListe=[1]
        fonction2(maListe, 2,10)
        fonction2(maListe, 2,5)
        fonction2(maListe, 2,12)
    duration = time() - start_time
    print("FN2 :",N, "Durée : ", duration)

for i in range(10) :
    evalFn1(10**i)
    evalFn2(10**i)
    print()