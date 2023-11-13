class Livre :
    def __init__( self , auteur , titre , nbPages ) :
        self.auteur = auteur
        self.titre = titre
        self.nbPages = nbPages
    def affiche(self) :
        print("Titre : " , self.titre )
        print("Auteur : ", self.auteur , " Pages : " , self.nbPages)

livre1 = Livre("Rousseau", "Les confessions de Rousseau", 1000)
livre2 = Livre("Stendhal", "Le rouge et le noir", 800)

livre1.affiche()
livre2.affiche()
