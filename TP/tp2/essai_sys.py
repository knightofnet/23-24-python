import sys
print(type(sys.argv))
print(sys.argv)

if len(sys.argv) < 3 :
	print("Erreur : le nombre de paramètres est insuffisant")
	exit()

n = int(sys.argv[1])
print("vous avez saisi ",n)  

z = int(sys.argv[2])

liste = [nombre ** z for nombre in range(1, n+1)]
somme = sum(liste)
	
print("La somme des carrés des entiers de 1 à",n," est ", somme)

