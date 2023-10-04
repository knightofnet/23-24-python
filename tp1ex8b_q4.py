from random import random

lNbLancers = [10, 100, 1000, 1E6]

for nb_lancers in lNbLancers :
	
	print("NbLancer :", nb_lancers)
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
