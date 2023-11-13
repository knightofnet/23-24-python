def sommeDesCarres(n) :
    s = 0
    for i in range(1, n+1) :
        s += i ** 2
    return s
    
def sommeDesInverse(n) :
    s = 0
    for i in range(1, n+1) :
        s += 1/i
    return s
    
print(sommeDesCarres(4))
assert sommeDesCarres(4) == 30

print(sommeDesInverse(10))