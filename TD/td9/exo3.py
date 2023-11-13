# Importation de la constante pi du module math
from math import pi

# Définition d'une classe nommée 'Cylindre'
class Cylindre :
    """Classe représentant un cylindre"""

    # Constructeur de la classe avec quatre paramètres : rayon, hauteur, couleur, et matiere
    # Les paramètres couleur et matiere ont des valeurs par défaut
    def __init__(self, rayon, hauteur, couleur="blanc", matiere="inconnu") :

        # Définition des attributs d'instances
        self.rayon = rayon    # Stocke le rayon du cylindre
        self.hauteur = hauteur  # Stocke la hauteur du cylindre
        self.couleur = couleur  # Stocke la couleur du cylindre, blanc par défaut
        self.matiere = matiere  # Stocke la matière du cylindre, inconnu par défaut

    # Méthode pour afficher les détails du cylindre
    def affich(self) :
        print(f"Cylindre [rayon: {self.rayon}, hauteur: {self.hauteur}, couleur: {self.couleur}, matiere: {self.matiere}]")

    # Méthode pour calculer le volume du cylindre
    def vol(self) :
        return pi * (self.rayon ** 2) * self.hauteur  # Formule du volume d'un cylindre
    
# Création d'instances de la classe Cylindre avec différentes caractéristiques
c1 = Cylindre(12, 32, "rouge", "pvc")
# Affichage des attributs de c1 et de la documentation de la classe
print("C1", c1.__dict__, c1.__doc__)

c2 = Cylindre(10, 2, "vert")
# Affichage des attributs de c2, de la documentation de la classe, et du volume du cylindre c2
print("C2", c2.__dict__, c2.__doc__)
print("C2", c2.vol())
c2.affich()

# Création d'une autre instance de Cylindre avec spécification explicite de la matière
c3 = Cylindre(10, 2, matiere="métal")
# Affichage du volume de c3 et de ses détails
print("C3", c3.vol())
c3.affich()
