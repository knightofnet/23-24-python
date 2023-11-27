carres_spec = [nbr ** 2 for nbr in range(11) if nbr != 5 and nbr != 8]
print(carres_spec)

#2 

liste_cubes = [nbr ** 3   for nbr in range(100 + 1)  if nbr % 2 != 0]
print(liste_cubes)

# 3
# Coder une fonction somme_puissance_impaire prenant 
# en paramètres deux entiers n et p, et
# renvoyant la somme des entiers impairs de 1 à n à la puissance p (1p+3p+...)
def somme_puissance_impaire(n, p) :
    liste = [nbr ** p   for nbr in range(n + 1)  if nbr % 2 != 0]    
    return sum(liste)

def somme_puissance_impaire_accu(n, p) :
    s = 0
    for nbr in range(n + 1) :
        if nbr %2 !=0 :
            s += nbr
    return s
    
p = somme_puissance_impaire(4, 2)
print(p)



