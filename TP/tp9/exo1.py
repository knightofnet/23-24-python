class Chat :
    "Représente un chat"

    def __init__(self, pNom, pRace, pPoids, pAnneeNaissance):
        self.nom = pNom
        self.race = pRace
        self.poids = pPoids
        self.anneeNaissance = pAnneeNaissance

    def affiche(self) :
        print("Chat [nom: {}, race: {}, poids: {}, année Naissance: {}]".format(self.nom, self.race, self.poids, self.anneeNaissance))

    def estPlusGros(self, autreChat) :
        if (isinstance(autreChat, Chat)) :
            if self.poids > autreChat.poids :
                print(self.nom, "est plus gros que ", autreChat.nom)
            elif self.poids < autreChat.poids :
                print(autreChat.nom, "est plus gros que ", self.nom )
            else :
                print(autreChat.nom, "et", self.nom, "ont le même poids" )

    def estPlusVieux(self, autreChat) :
        if self.anneeNaissance < autreChat.anneeNaissance :
            print(self.nom, "est plus vieux que ", autreChat.nom)
        elif self.anneeNaissance > autreChat.anneeNaissance :
            print(autreChat.nom, "est plus vieux que ", self.nom )
        else :
            print(autreChat.nom, "et", self.nom, "ont le même age" )

c1 = Chat("Félix", "maincoon", 14, 2018)
c2 = Chat("Garfield", "exotic shorthair", 14, 2020)

print(c1)
print(c2)

c1.affiche()
c2.estPlusGros(c1)
c2.estPlusVieux(c1)


 