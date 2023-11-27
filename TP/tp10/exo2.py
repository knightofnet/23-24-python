class Inventaire(dict):
    
    def __str__(self) :
        lstClefs = list(self.keys())
        lstClefs.sort()

        retour = []
        for clef in lstClefs :
            chaine = f"{clef}:{self[clef]}"
            retour.append(chaine)

        return "{" + ", ".join(retour) + "}"

    def __add__(self, o) :

        d = {}
        clefs = list( set( list(self.keys()) + list(o.keys()) )   )

        for clef in clefs :
            d[clef] = self.get(clef, 0) + o.get(clef, 0)

        return Inventaire(d)

inv1 = Inventaire({'pâtes' : 2 , 'farine': 1 })
inv2 = Inventaire({'pâtes' : 2 , 'lessive' : 2})

inv3 = inv1 + inv2
print(inv3)