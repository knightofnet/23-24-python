class Voiture :
    "Représente une voiture"

    def __init__(self, pMarque, pModele) :
        self.marque = pMarque
        self.modele = pModele
        self.kilometrage = 0

    def roule(self, km) :
        self.kilometrage += km

    def affiche(self) :
        print("Voiture [marque: {}, modele: {}, kilometrage: {}]".format(self.marque, self.modele, self.kilometrage))

v1 = Voiture("Toyota", "Auris")
v1.roule(100)
v1.affiche()

v2 = Voiture("Renault", "Scenic")
v3 = Voiture("Citroen", "C3")

v2.roule(150)
v3.roule(250)

v2.affiche()
v3.affiche()