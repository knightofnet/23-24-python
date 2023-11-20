# Import de la constante pi du module math
from math import pi

# Définition d'une classe nommée 'Cylindre'
class Cylindre :
    """Classe représentant un cylindre"""

    # Constructeur de la classe avec quatre paramètres : rayon, hauteur, couleur
    # Les paramètres couleur et matiere ont des valeurs par défaut
    def __init__(self, rayon, hauteur, couleur="blanc") :

        # Définition des attributs d'instances
        self.rayon = rayon    # Stocke le rayon du cylindre
        self.hauteur = hauteur  # Stocke la hauteur du cylindre
        self.couleur = couleur  # Stocke la couleur du cylindre, blanc par défaut

    # Méthode pour afficher les détails du cylindre
    def __str__(self) :
        return f"Cylindre [rayon: {self.rayon}, hauteur: {self.hauteur}, couleur: {self.couleur}]"

    # Méthode pour calculer le volume du cylindre
    def vol(self) :
        return pi * (self.rayon ** 2) * self.hauteur  # Formule du volume d'un cylindre
    
    def __eq__(self, autre) :
        return self.rayon == autre.rayon and self.hauteur == autre.hauteur and self.couleur == autre.couleur
    
    def __lt__(self, autre) :
        return self.vol() < autre.vol()
    
    def __le__(self, autre) :
        return self.vol() <= autre.vol()

c1=Cylindre(1,1)
c2=Cylindre(2,2)
print('c1=c2 - attendu : False, observé :', c1==c2)
print('c1=Cylindre(1, 1) - attendu : True, observé :', c1==Cylindre(1, 1))
print('c1!=c2 - attendu : True, observé :', c1!=c2)

print('c1<c2 - attendu : True, observé :',c1<c2)
print('c2<c2 - attendu : False, observé :',c2<c2)
print('c2<=c2 - attendu : True, observé :',c2<=c2)
print('c2>c2 - attendu : False, observé :',c2>c2)
print('c2>=c2 - attendu : False, observé :',c2>=c2)

print('c1<=c2 - attendu : True, observé :',c1<=c2)


