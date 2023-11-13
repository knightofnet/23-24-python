def factoriel(n) :
    s = 1
    for i in range(1, n+1) :
        s = s * i
    return s
    
v = factoriel(5)
print(v)

assert factoriel(5) == 120