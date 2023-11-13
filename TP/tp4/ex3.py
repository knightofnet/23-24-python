def factoriel(n) :
    f=1
    for i in range(2,n+1) :
        f=f*i
    return f

def fnC(p, n) :
    return factoriel(n) / ( factoriel(p) * factoriel( n - p) )

def dev(n) :
    print("(a + b)^", n, " = a^", n, " + ", sep='', end='')
    
    for i in range(1, n ) :
        c = fnC(i, n)
        puissanceA = n - i
        puissanceB = i
        print(int(c), " a^", puissanceA, " b^", puissanceB, " + ", end='', sep='')
      
    print("b^", n, sep='')
dev(4)

# appel de la fonction fnC()
"""
n = int(input("veuillez saisir n"))
p = int(input("veuillez saisir p"))
while p < 0 or p > n :
    p = int(input("veuillez saisir p"))    

print(fnC(p,n))

assert fnC(5,8) == 56
"""


