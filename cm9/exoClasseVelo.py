class Velo :
    def __init__(self, pModele, pNbVitesse, pAnnee) :
        self.modele = pModele
        self.nbVitesse = pNbVitesse
        self.annee = pAnnee

    def affiche(self) :
        print("Modele: {}, NbVitesse: {}, annee: {} ".format(self.modele, self.nbVitesse, self.annee))

v1 = Velo("Rockrider 320", 21, 2002)
v2 = Velo("Btwin", 18, 2012)

v1.affiche()
v2.affiche()