# Définition de la classe Inventaire qui hérite de la classe intégrée dict (dictionnaire)
class Inventaire(dict):
    
    # Méthode spéciale pour définir la représentation en chaîne de caractères de l'objet Inventaire
    def __str__(self):
        # Obtention et tri des clés du dictionnaire
        lstClefs = list(self.keys())
        lstClefs.sort()

        # Construction d'une liste de chaînes de caractères pour chaque paire clé:valeur
        retour = []
        for clef in lstClefs:
            # Formatage de chaque paire clé:valeur
            chaine = f"{clef}:{self[clef]}"
            retour.append(chaine)

        # Concaténation des chaînes de caractères pour former une représentation de type dictionnaire
        return "{" + ", ".join(retour) + "}"

    # Méthode spéciale pour surcharger l'opérateur '+'
    def __add__(self, o):
        # Création d'un nouveau dictionnaire vide
        d = {}

        # Création d'une liste unique des clés des deux inventaires (self et o)
        clefs = list(set(list(self.keys()) + list(o.keys())))

        # Calcul des sommes pour chaque clé des deux inventaires
        for clef in clefs:
            d[clef] = self.get(clef, 0) + o.get(clef, 0)

        # Retour d'un nouvel objet Inventaire contenant la somme des éléments des deux inventaires
        return Inventaire(d)

# Création d'instances de la classe Inventaire
inv1 = Inventaire({'pâtes': 2, 'farine': 1})
inv2 = Inventaire({'pâtes': 2, 'lessive': 2})

# Utilisation de la surcharge de l'opérateur '+' pour combiner deux inventaires
inv3 = inv1 + inv2

# Affichage du nouvel inventaire combiné
print(inv3)
