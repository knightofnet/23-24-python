def testA(n) :
    n += 1
    print("  n vaut", n)
    print("  adresse mémoire n :", id(n))

p = 3
print("adresse mémoire p :", id(p))

testA(p)
print("p vaut :", p)
print("adresse mémoire p :", id(p))