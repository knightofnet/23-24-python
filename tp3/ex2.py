
def termeSuite1 (m,n) :
    u=m
    print("u 0=", u)
    for i in range(1,n+1) :        
        u = u**2 - 5
        print("u",i, "=", u)
    return u

def sommeTermes(n,x) :
    u = x
    s = x
    
    for i in range(1,n + 1) :
        u = 3/u
        s = s + u
        
    return s
#print(termeSuite1(4,3))

print(sommeTermes(5, 3.2))
# 12.412500000000001
