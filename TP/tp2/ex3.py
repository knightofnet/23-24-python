"""
n = int(input("entrer un entier : "))
print("vous avez saisi ",n)

p = int(input("entrer la puissance : "))

s = 0
for i in range(1, n + 1) :
	s = s + i ** p

print(s)
"""
liste=[]
for nombre in range(1,4) :
	liste.append(nombre ** 2)
print(liste)

print([nombre ** 2   for nombre in range(1, 4)])
print(sum(  [nombre ** 2 for nombre in range(1, 4)]  ))




n = int(input("entrer un entier : "))
print("vous avez saisi ",n)
p = int(input("entrer la puissance : "))

s = 0
for i in range(1, n + 1) :
	s = s + i ** p
print(s)


L=[]
for i in range(1, n + 1) :
	L.append( i ** p)
print(sum(L))


print( sum( [ i ** p    for i in range(1, n + 1) ]) )






