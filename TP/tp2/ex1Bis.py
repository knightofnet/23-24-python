"""
chaine_1 = "123"
chaine_2 = "346"
print(chaine_1 + chaine_2)
print(str(int(chaine_1) + int(chaine_2)))
print(type( str(int(chaine_1) + int(chaine_2)) ))

# la fonction int() transforme des objets en entier.
# exemple : int('123') = 123

# la fonction str() transforme des objets en chaine de caractères.

print(int(12.3),";",int(34.6))

chaine_1 = "12.3"
chaine_2 = "34.6"
print(str(float(chaine_1) + float(chaine_2)))
# la fonction float() transforme des objets en réel.
# exemple : float('12.3') = 12.3
"""

chaine = "abcdefgh"
liste_a = list(chaine)
tuple_a = tuple(chaine)
tuple_b = tuple(liste_a)
liste_b = list(tuple_a)
print("liste_a:", liste_a)
print("liste_b:", liste_b)
print("tuple_a:", tuple_a)
print("tuple_b:",tuple_b)



