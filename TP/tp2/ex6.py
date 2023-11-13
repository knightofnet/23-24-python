taille_limite = 1000
resultats = list()
for candidat in range(2, taille_limite+1):
	estPremier = True
	for nombre_1 in range(2, candidat):

		if candidat % nombre_1 == 0:
			estPremier = False
	
	if estPremier == true :
		resultats.append(candidat)

print(resultats)
