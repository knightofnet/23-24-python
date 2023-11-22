class Chien :
    def __init__(self, pIdentification, pNom, pRace, pDatenaiss, pTaille=0, pPoids=0) :
        self.identification = pIdentification
        self.nom = pNom        
        self.race = pRace      
        self.dateNaiss = pDatenaiss
        self.taille = pTaille  
        self.poids = pPoids 

    def affiche(self) :
        print(f"{self.nom} est un chien de race {self.race}")
        print(f"Il est né le {self.dateNaiss[0]} / {self.dateNaiss[1]} / {self.dateNaiss[2]}")
        print(f"Il mesure {self.taille} cm")
        
        if (self.poids > 0) :
            print(f"Il pèse {self.poids} cm")

        if ("P" == self.identification[0]) :
            print(f"Il a une puce d'identification : {self.identification[1:]}")
        elif ("T" == self.identification[0]) :
            print(f"Il est tatoué : {self.identification[1:]}")

class Candidat(Chien) :

    lstConcoursConnus = []

    def __init__(self, pIdentification, pNom, pRace, pDatenaiss, pTaille=0, pPoids=0, concours=[]):
        Chien.__init__(self, pIdentification, pNom, pRace, pDatenaiss, pTaille, pPoids)
        self.concours = concours

        Candidat.lstConcoursConnus.extend(concours)
        Candidat.lstConcoursConnus = list(set(Candidat.lstConcoursConnus))

    def affiche(self):
        super().affiche()
        print(f"il a participé à {len(self.concours)} concours :")
        for concour in self.concours :
            print(f"    {concour}")

    def participe(self, nomConcour) :
        self.concours.append(nomConcour) 
        Candidat.lstConcoursConnus.append(nomConcour)
        Candidat.lstConcoursConnus = list(set(Candidat.lstConcoursConnus))

    @classmethod
    def concoursConnus(cls) :
        print("Voici les concours que nous avons répertoriés:", cls.lstConcoursConnus)

c1 = Chien("P250263890203125","Tara","Bichon",(2,5,2022),25.5)
c2 = Chien("TAG896","Sophia","Berger",(3,6,2021),48,5.6)

# c1.affiche()
# c2.affiche()

cand1 = Candidat("P250261992073142","Sangdor","Caniche",(12,6,2021),31.5,3.1,["Tours canin 2022","Mon chien 2022"])
cand1.participe("Concours canin Langeais 2022")
cand1.affiche()

cand2 = Candidat("P250261920341256","Tador","Caniche",(1,5,2022),28.5,2.9,["Mon chien 2022","os d'or 2022"])

Candidat.concoursConnus()

