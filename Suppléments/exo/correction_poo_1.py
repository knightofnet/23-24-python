# Définition de la classe Etudiant
class Etudiant:

    # Liste de classe pour stocker tous les étudiants créés
    listeEtudiants = []

    # Constructeur de la classe Etudiant
    def __init__(self, nom, numEtud, moyenne):
        self.nom = nom  # Attribut pour le nom de l'étudiant
        self.numEtud = numEtud  # Attribut pour le numéro d'étudiant
        self.moyenne = moyenne  # Attribut pour la moyenne de l'étudiant

        # Ajoute l'instance actuelle à la liste des étudiants
        Etudiant.listeEtudiants.append(self)

    # Méthode pour afficher les informations d'un étudiant
    def affiche(self):
        print(f"Étudiant : {self.nom}\nNuméro d'étudiant : {self.numEtud}\nMoyenne : {self.moyenne}")

    # Méthode statique pour déterminer la mention en fonction de la moyenne
    @staticmethod
    def mention(moyenne):
        if moyenne >= 16:
            return "Très bien"
        if 14 <= moyenne < 16:
            return "Bien"
        if 12 <= moyenne < 14:
            return "Assez bien"
        return "Insuffisant"
    
    # Méthode pour mettre à jour la moyenne d'un étudiant
    def miseAJourMoyenne(self, lstNotes):
        nvlMoyenne = (sum(lstNotes) + self.moyenne) / (len(lstNotes) + 1)
        self.moyenne = nvlMoyenne

    # Méthode de classe pour supprimer un étudiant par son numéro
    @classmethod
    def supprimerEtudiant(cls, numero):
        for etudiant in cls.listeEtudiants:
            if etudiant.numEtud == numero:
                cls.listeEtudiants.remove(etudiant)
                break

    # Méthode pour supprimer l'instance actuelle de la liste des étudiants
    def supprimerEtudiantInstance(self):
        for etudiant in Etudiant.listeEtudiants:
            if etudiant.numEtud == self.numEtud:
                Etudiant.listeEtudiants.remove(etudiant)
                break

# Classe EtudiantBoursier, héritant de la classe Etudiant
class EtudiantBoursier(Etudiant):

    # Constructeur de la classe EtudiantBoursier
    def __init__(self, nom, numEtud, moyenne, estBoursier):
        Etudiant.__init__(self, nom, numEtud, moyenne)  # Appel au constructeur de la classe mère
        self.estBoursier = estBoursier  # Attribut pour déterminer si l'étudiant est boursier

    # Méthode surchargée pour afficher les informations d'un étudiant boursier
    def affiche(self):
        super().affiche()  # Appel à la méthode de la classe parente
        estBoursierStr = "Non"
        if self.estBoursier == True :
            estBoursierStr = "Oui"
        print("Bourse :", estBoursierStr)

# Création d'une instance de la classe Etudiant
e1 = Etudiant("Alice", 12345, 17.5)
# Création d'une instance de la classe EtudiantBoursier
e2 = EtudiantBoursier("Bob", 12346, 12.5, True)

# Affichage des informations de l'étudiant boursier
e2.affiche()

# Suppression de l'étudiant e1 par le biais de la méthode de classe
Etudiant.supprimerEtudiant(e1.numEtud)
# Suppression de l'étudiant e2 par le biais de la méthode d'instance
e2.supprimerEtudiantInstance()

# Tentative d'affichage des informations de e1
e1.affiche()  # Cela fonctionnera car l'objet e1 existe toujours, même s'il a été supprimé de la liste

# Mise à jour de la moyenne de e1
e1.miseAJourMoyenne([0, 20])
# Affichage des informations mises à jour de e1
e1.affiche()
