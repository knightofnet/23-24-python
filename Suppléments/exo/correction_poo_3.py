class Livre :

    def __init__(self, titre, auteur, isbn) :
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

        if not(Livre.verifISBN(self.isbn)) :
            raise ValueError("ISBN faux")

    def __str__(self) :
        return str(self.__dict__)
    
    @staticmethod
    def verifISBN(isbn) :
        if len(isbn) != 10 :
            return False
        
        if not(isbn[0:9].isdigit()) :
            return False
        
        if not(isbn[-1].isdigit()) and isbn[-1] != "X" :
            return False
        
        s = 0
        for i,c in enumerate(isbn) :
            p = 0
            if i < 9 :
                p = int(c)
            else : 
                if c == "X" :
                    p = 10
                else :
                    p = int(c)
            s += p * (i + 1)

        if s % 11 != 0 :
            return False
        
        return True
    

class Bibliotheque :

    def __init__(self, nom) -> None:
        self.nom = nom
        self.livres = {}

    def ajouterLivre(self, livre) :
        if livre is self.livres :
            return
        
        self.livres[livre.isbn] = livre

    def rechercheLivre(self, isbn) :
        return isbn in self.livres

livre1 = Livre("Apprendre Python", "Swinen", "123456789X")
livre2 = Livre("Da Vinci Code", "D.Brown", "123456789X")

print(livre1)






def verifISBN(isbn) :
    if len(isbn) != 10 :
        return False
    
    produitVerif = 0
    for i, c in enumerate(isbn) :

        intC = 0

        if (i < 10) :
            if (c < "0" or c > "9") :
                return False
            else :
                intC = int(c)
        else :
            if (c != "X" or c < "0" or c > "9") :
                return False
            else :
                if (c == "X") :
                    intC = 10
                else :          
                    intC = int(c)
        


         