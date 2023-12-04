class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.emprunts = {}

    def ajouter_livre(self, titre, nombre):
        if titre in self.livres:
            self.livres[titre] += nombre
        else:
            self.livres[titre] = nombre
            self.emprunts[titre] = 0

    def emprunter_livre(self, titre):
        if titre in self.livres and self.livres[titre] > 0:
            self.livres[titre] -= 1
            self.emprunts[titre] += 1
        else:
            raise ValueError("Le livre n'est pas disponible")

    def retourner_livre(self, titre):
        if titre in self.emprunts and self.emprunts[titre] > 0:
            self.livres[titre] += 1
            self.emprunts[titre] -= 1
        else:
            raise ValueError("Le livre n'a pas été emprunté")

    def __str__(self):
        chaine = "État de la bibliothèque:"
        for titre in self.livres:
            chaine += f"{titre} - Disponibles: {self.livres[titre]}, Empruntés: {self.emprunts[titre]}"
        return chaine


# Corps pricipal :
# ================

# Création de l'instance de la bibliothèque
maBibliotheque = Bibliotheque()

# Ajout de livres à la bibliothèque
maBibliotheque.ajouter_livre("Le Petit Prince", 5)
maBibliotheque.ajouter_livre("1984", 3)
maBibliotheque.ajouter_livre("Harry Potter", 2)

# Vérification que les livres ont été ajoutés correctement
assert "Le Petit Prince" in maBibliotheque.livres
assert maBibliotheque.livres["Le Petit Prince"] == 5
assert maBibliotheque.livres["1984"] == 3
assert maBibliotheque.livres["Harry Potter"] == 2

# Emprunt de livres
maBibliotheque.emprunter_livre("Le Petit Prince")
maBibliotheque.emprunter_livre("1984")

# Vérification que les livres ont été empruntés correctement
assert maBibliotheque.livres["Le Petit Prince"] == 4
assert maBibliotheque.emprunts["Le Petit Prince"] == 1
assert maBibliotheque.livres["1984"] == 2
assert maBibliotheque.emprunts["1984"] == 1

# Tentative d'emprunt d'un livre non disponible
try:
    maBibliotheque.emprunter_livre("Un livre inexistant")
    assert False, "Une exception ValueError aurait dû être levée"
except ValueError as e:
    assert str(e) == "Le livre n'est pas disponible"

# Retour de livres
maBibliotheque.retourner_livre("Le Petit Prince")

# Vérification que les livres ont été retournés correctement
assert maBibliotheque.livres["Le Petit Prince"] == 5
assert maBibliotheque.emprunts["Le Petit Prince"] == 0

# Tentative de retour d'un livre jamais emprunté
try:
    maBibliotheque.retourner_livre("Un livre jamais emprunté")
    assert False, "Une exception ValueError aurait dû être levée"
except ValueError as e:
    assert str(e) == "Le livre n'a pas été emprunté"

assert isinstance(str(maBibliotheque), str)

print("Tous les tests ont réussi !")