# Définition d'une classe nommée 'Livre'
class Livre :
    # Constructeur de la classe avec trois paramètres : auteur, titre, et nbPages
    def __init__( self , auteur , titre , nbPages ) :

        # Assignation des paramètres à des variables d'instance (attributs de l'instance)
        self.auteur = auteur  # Stocke l'auteur du livre
        self.titre = titre    # Stocke le titre du livre
        self.nbPages = nbPages  # Stocke le nombre de pages du livre

    # Méthode d'instance pour afficher les détails du livre
    def affiche(self) :
        # Affiche le titre du livre
        print("Titre : " , self.titre )
        # Affiche l'auteur et le nombre de pages du livre
        print("Auteur : ", self.auteur , " Pages : " , self.nbPages)

# Création d'une instance de la classe Livre avec les détails de l'auteur, du titre et du nombre de pages
livre1 = Livre("Rousseau", "Les confessions de Rousseau", 1000)
# Création d'une seconde instance de la classe Livre
livre2 = Livre("Stendhal", "Le rouge et le noir", 800)

# Appel de la méthode affiche pour l'instance livre1
livre1.affiche()
# Appel de la même méthode pour l'instance livre2
livre2.affiche()
