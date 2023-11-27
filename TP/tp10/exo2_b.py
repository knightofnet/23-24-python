class Inventaire():
    
    def __init__(self, nom, inventaire={}) :
        self.nom = nom
        self.inventaire = inventaire

    def __str__(self) :
        lstClefs = list(self.inventaire.keys())
        lstClefs.sort()

        retour = []
        for clef in lstClefs :
            chaine = f"{clef} : {self.inventaire[clef]} kg"
            retour.append(chaine)

        return f"Inventaire {self.nom}\n" +  "\n".join(retour)

    def __add__(self, o) :

        nouveauNom = f"{self.nom} + {o.nom}"
        dicoNouvelInventaire = {}
        clefs = list( set( list(self.inventaire.keys()) + list(o.inventaire.keys()) )   )

        for clef in clefs :
            dicoNouvelInventaire[clef] = self.inventaire.get(clef, 0) + o.inventaire.get(clef, 0)

        return Inventaire(nouveauNom, dicoNouvelInventaire)

inv1 = Inventaire("magasin 1", {'pâtes' : 2 , 'farine': 1 })
inv2 = Inventaire("magasin 2", {'pâtes' : 2 , 'lessive' : 2})

inv3 = inv1 + inv2
print(inv3)