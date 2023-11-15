class Vecteur :

    def __init__(self, x=0, y=0) :
        self.coord = (x, y)

    def affiche(self) :
        print(f"({self.coord[0]}, {self.coord[1]})")
        #print("({}, {})".format(self.coord[0], self.coord[1]))

    def x(self) :
        return self.coord[0]

    def y(self) :
        return self.coord[1]

    def prodScal(self, autreVecteur) :
        return self.x() * autreVecteur.x() + self.y() * autreVecteur.y()
    
    def somme(self, autreVecteur) :
        nouveauX = self.x() + autreVecteur.x()
        nouveauY = self.y() + autreVecteur.y()
        return Vecteur(nouveauX, nouveauY)

v1 = Vecteur(2, 2)
v2 = Vecteur(3, 3)

prodScal = v1.prodScal(v2)
print(prodScal)

v3 = v1.somme(v2)
v3.affiche()