from random import randint
minimum, maximum = -10, 10
nb_iterations = 100
compteur = 0
while compteur < nb_iterations:
	compteur = compteur + 1
	a, b, c, d = (randint(minimum, maximum),
		randint(minimum, maximum),
		randint(minimum,maximum), 
		randint(minimum,maximum))	

	while c == 0 :		
		c = randint(minimum,maximum)

	if a*b / c*d != (((a * b)/c) * d):
		print("L'identité est fausse!")
		

print('fin du pgm')
