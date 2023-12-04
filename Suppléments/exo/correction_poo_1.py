class Etudiant :

    listeEtudiants = []

    def __init__(self, nom, numEtud, moyenne) :
        self.nom = nom
        self.numEtud = numEtud
        self.moyenne = moyenne

        Etudiant.listeEtudiants.append(self)

    def affiche(self) :
        print(f"Étudiant : {self.nom}\nNuméro d'étudiant : {self.numEtud}\nMoyenne : {self.moyenne}")

    @staticmethod
    def mention(moyenne) :
        if moyenne >= 16 :
            return "Très bien"
        if 14 <= moyenne < 16 :
            return "Bien"
        if 12 <= moyenne < 14 :
            return "Assez bien"
        return "Insuffisant"
    
    def miseAJourMoyenne(self, lstNotes) :
        nvlMoyenne = (sum(lstNotes) + self.moyenne ) / (len(lstNotes) + 1)
        self.moyenne = nvlMoyenne

    @classmethod
    def supprimerEtudiant(cls, numero) :
        for etudiant in cls.listeEtudiants :
            if etudiant.numEtud == numero :
                cls.listeEtudiants.remove(etudiant)
                break

    def supprimerEtudiantInstance(self) :
        for etudiant in Etudiant.listeEtudiants :
            if etudiant.numEtud == self.numEtud :
                Etudiant.listeEtudiants.remove(etudiant)
                break

class EtudiantBoursier (Etudiant) :

    def __init__(self, nom, numEtud, moyenne, estBoursier):
        Etudiant.__init__(self, nom, numEtud, moyenne)
        self.estBoursier = estBoursier

    def affiche(self):
        super().affiche()
        estBoursierStr = "Non"
        if self.estBoursier == True :
            estBoursierStr = "Oui"
        print("Bourse :", estBoursierStr)

e1 = Etudiant("Alice", 12345, 17.5)
e2 = EtudiantBoursier("Bob", 12346, 12.5, True)
e2.affiche()

Etudiant.supprimerEtudiant(e1.numEtud)
e2.supprimerEtudiantInstance()
e1.affiche()
#e2.affiche()

#print(Etudiant.mention(13))

e1.miseAJourMoyenne([0, 20])
e1.affiche()