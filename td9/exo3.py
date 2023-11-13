from math import pi

class Cylindre :
    """Classe représentant un cylindre"""

    def __init__(self, rayon, hauteur, couleur="blanc", matiere="inconnu") :
        self.rayon = rayon
        self.hauteur = hauteur
        self.couleur = couleur
        self.matiere = matiere 

    def affich(self) :
        print(f"Cylindre [rayon: {self.rayon}, hauteur: {self.hauteur}, couleur: {self.couleur}, matiere: {self.matiere}]")

    def vol(self) :
        return pi * (self.rayon ** 2) * self.hauteur
    
c1 = Cylindre(12, 32, "rouge", "pvc")
print("C1", c1.__dict__, c1.__doc__)

c2 = Cylindre(10, 2, "vert")
print("C2", c2.__dict__, c2.__doc__)
print("C2", c2.vol())
c2.affich()

c3 = Cylindre(10, 2, matiere="métal")
print("C3", c3.vol())
c3.affich()