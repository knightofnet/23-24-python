def cube(lon):
    """ calcul du volume et de l'aire """
    vol = lon**3
    surf = (lon**2)*6
    return (vol,surf)

"""
c = int(input("longueur de l'arête du cube ? "))
(v,s)=cube(c)
print("volume : ",v," surface : ",s)
"""

def affiche(n):
    for i in range(1,n+1):
        (v,s)=cube(i)
        print("cube de côté ",i," : volume ",v," surface",s)
"""
p = int(input("Saisir un entier : "))
affiche(p)
"""

from math import pi

def sphere(r) :
    "calcul du volume et de la surface d'une sphere de rayon r"
    vol = (4/3) * pi * r ** 3
    s = 4 * pi * r ** 2
    return (vol, s)

def afficheSphere(n):
    for i in range(1,n+1):
        (v,s)=sphere(i)
        print("sphere de rayon ",i," : volume ",round(v, 2)," surface", round(s, 2))

p = 3
afficheSphere(p)