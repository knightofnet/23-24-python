"""
n = int(input("entrer un entier : "))
print("vous avez saisi ",n)  


z = int(input("entrer la puissance :"))


somme = 0
for i in range(1, n + 1) :
	somme = somme + i ** z
	
print("La somme des carrés des entiers de 1 à",n," est ", somme)
"""
"""
liste=[]
for nombre in range(1,4) :
	liste.append( nombre ** 2)
print(liste)

print([nombre for nombre in range(1, 4)])
"""

n = int(input("entrer un entier : "))
print("vous avez saisi ",n)  

z = int(input("entrer la puissance :"))

liste = [nombre ** z for nombre in range(1, n+1)]
somme = sum(liste)
	
print("La somme des carrés des entiers de 1 à",n," est ", somme)




