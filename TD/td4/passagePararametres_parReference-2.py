def testB(a) :
    a[1] = 99
    print("  a :", a)
    print("  adresse mémoire a :", id(a))

tab = [2, 6, 8, 5]
print("adresse mémoire tab :", id(tab))

testB(tab)

print(tab)
print("adresse mémoire tab :", id(tab))
