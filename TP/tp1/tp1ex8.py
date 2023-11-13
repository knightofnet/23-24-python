from random import random
nb_lancers = 10
compteur = 0
nb_pile=0
while compteur < nb_lancers:
	compteur = compteur + 1
	alea = random()
		
	if 0.3 < alea < 0.5 :
		continue
		
	print("test")

print(nb_pile, compteur, nb_pile / nb_lancers)
