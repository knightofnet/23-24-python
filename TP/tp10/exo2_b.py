# Définition de la classe Inventaire
class Inventaire():
    
    # Constructeur de la classe avec deux paramètres : nom et inventaire
    def __init__(self, nom, inventaire={}):
        self.nom = nom  # Nom de l'inventaire
        self.inventaire = inventaire  # Dictionnaire représentant l'inventaire (clé: article, valeur: poids)

    # Méthode spéciale pour définir la représentation en chaîne de caractères de l'objet Inventaire
    def __str__(self):
        # Obtention et tri des clés du dictionnaire inventaire
        lstClefs = list(self.inventaire.keys())
        lstClefs.sort()

        # Construction d'une liste de chaînes de caractères représentant chaque article et son poids
        retour = []
        for clef in lstClefs:
            chaine = f"{clef} : {self.inventaire[clef]} kg"
            retour.append(chaine)

        # Assemblage des chaînes de caractères en une seule, séparées par des retours à la ligne
        return f"Inventaire {self.nom}\n" + "\n".join(retour)

    # Méthode spéciale pour surcharger l'opérateur '+'
    def __add__(self, o):
        # Création d'un nouveau nom pour l'inventaire combiné
        nouveauNom = f"{self.nom} + {o.nom}"

        # Initialisation d'un nouveau dictionnaire pour le nouvel inventaire
        dicoNouvelInventaire = {}

        # Création d'une liste unique des clés des deux inventaires
        clefs = list(set(list(self.inventaire.keys()) + list(o.inventaire.keys())))

        # Calcul des sommes des poids pour chaque article des deux inventaires
        for clef in clefs:
            dicoNouvelInventaire[clef] = self.inventaire.get(clef, 0) + o.inventaire.get(clef, 0)

        # Retour d'un nouvel objet Inventaire combinant les deux inventaires
        return Inventaire(nouveauNom, dicoNouvelInventaire)

# Création d'instances de la classe Inventaire
inv1 = Inventaire("magasin 1", {'pâtes': 2, 'farine': 1})
inv2 = Inventaire("magasin 2", {'pâtes': 2, 'lessive': 2})

# Utilisation de la surcharge de l'opérateur '+' pour combiner deux inventaires
inv3 = inv1 + inv2

# Affichage du nouvel inventaire combiné
print(inv3)
