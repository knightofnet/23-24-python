from random import random

nb_lancers = 1000000
compteur = 0
nb_pile = 0

while compteur < nb_lancers:
	compteur = compteur + 1
	alea = random()
	if alea < 0.5:
		#print("Pile")
		nb_pile += 1 
	else:
		pass
		#print("Face")

print(nb_pile / nb_lancers)
