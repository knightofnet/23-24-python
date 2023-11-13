def fct(n) :
    m = 2*n
    return (n,m)

def division_euclidienne(a, b) :
    q = 0
    r = a 
    
    while r >= b :
        q = q + 1
        r = r - b
    
    return (q,r)

def question2() :
    
    nbErreur = 0
    if (division_euclidienne(19, 5) != (3,4)) :
        nbErreur += 1
        
    if (division_euclidienne(20, 5) != (4,0)) :
        nbErreur += 1    
        
    if (division_euclidienne(152, 5) != (24,5)) :
        nbErreur += 1           
        
    if (division_euclidienne(2578, 55) != (32,1)) :
        nbErreur += 1 
        
    if nbErreur > 0 :
        print("il y a des erreurs")
    else :
        print("il n'y a pas d'erreur")
    


from random import randint

def verification_automatique() :
    
    nbErreur = 0
    
    for i in range(100) :
        q = randint(0, 1000)
        b = randint(0, 1000)
        r = randint(0, b - 1)
       
        a = b * q + r
        if (division_euclidienne(a, b) != (q, r)) :
            nbErreur += 1
            
    if nbErreur > 0 :
        print("il y a des erreurs")
        return False
    
    print("il n'y a pas d'erreur")
    return True
    

print(verification_automatique())
