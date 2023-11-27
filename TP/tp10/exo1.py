# Définition de la classe Chien
class Chien:
    # Méthode d'initialisation (constructeur) de la classe Chien
    def __init__(self, pIdentification, pNom, pRace, pDatenaiss, pTaille=0, pPoids=0):
        # Initialisation des attributs de l'instance
        self.identification = pIdentification  # Identifiant unique du chien
        self.nom = pNom                         # Nom du chien
        self.race = pRace                       # Race du chien
        self.dateNaiss = pDatenaiss             # Date de naissance du chien (tuple)
        self.taille = pTaille                   # Taille du chien en cm
        self.poids = pPoids                     # Poids du chien en kg

    # Méthode pour afficher les informations d'un chien
    def affiche(self):
        print(f"{self.nom} est un chien de race {self.race}")
        # Affichage formaté de la date de naissance
        print(f"Il est né le {self.dateNaiss[0]} / {self.dateNaiss[1]} / {self.dateNaiss[2]}")
        print(f"Il mesure {self.taille} cm")
        
        # Condition pour vérifier si le poids est spécifié
        if self.poids > 0:
            print(f"Il pèse {self.poids} kg")

        # Condition pour vérifier le type d'identification (puce ou tatouage)
        if "P" == self.identification[0]:
            print(f"Il a une puce d'identification : {self.identification[1:]}")
        elif "T" == self.identification[0]:
            print(f"Il est tatoué : {self.identification[1:]}")

# Définition de la classe Candidat qui hérite de la classe Chien
class Candidat(Chien):
    # Attribut de classe pour conserver la liste des concours connus
    lstConcoursConnus = []

    # Méthode d'initialisation (constructeur) de la classe Candidat
    def __init__(self, pIdentification, pNom, pRace, pDatenaiss, pTaille=0, pPoids=0, concours=[]):
        # Appel au constructeur de la classe parent (Chien)
        super().__init__(pIdentification, pNom, pRace, pDatenaiss, pTaille, pPoids)
        self.concours = concours  # Liste des concours auxquels le chien a participé

        # Mise à jour de la liste des concours connus
        Candidat.lstConcoursConnus.extend(concours)
        Candidat.lstConcoursConnus = list(set(Candidat.lstConcoursConnus))

    # Méthode pour afficher les informations du candidat
    def affiche(self):
        # Appel à la méthode affiche de la classe parent (Chien)
        super().affiche()
        print(f"il a participé à {len(self.concours)} concours :")
        for concour in self.concours:
            print(f"    {concour}")

    # Méthode pour ajouter un nouveau concours à la liste du candidat
    def participe(self, nomConcour):
        self.concours.append(nomConcour) 
        Candidat.lstConcoursConnus.append(nomConcour)
        Candidat.lstConcoursConnus = list(set(Candidat.lstConcoursConnus))

    # Méthode de classe pour afficher tous les concours connus
    @classmethod
    def concoursConnus(cls):
        print("Voici les concours que nous avons répertoriés:", cls.lstConcoursConnus)

# Création d'instances de la classe Chien et utilisation des méthodes
c1 = Chien("P250263890203125", "Tara", "Bichon", (2, 5, 2022), 25.5)
c2 = Chien("TAG896", "Sophia", "Berger", (3, 6, 2021), 48, 5.6)

# Création d'instances de la classe Candidat, sous-classe de Chien
cand1 = Candidat("P250261992073142","Sangdor","Caniche",(12,6,2021),31.5,3.1,["Tours canin 2022","Mon chien 2022"])
# Fais participer le candidat Sangdaor, cand1, au concours : Concours canin Langeais 2022
cand1.participe("Concours canin Langeais 2022")

cand1.affiche()

cand2 = Candidat("P250261920341256","Tador","Caniche",(1,5,2022),28.5,2.9,["Mon chien 2022","os d'or 2022"])

# Affichage des concours connus
Candidat.concoursConnus()
