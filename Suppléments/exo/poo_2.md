## Exercice entrainement 2

Dans cet exercice, vous allez créer une classe `Bibliothèque` qui gère les livres et les emprunts. L'exercice comprend trois questions, de la question A à la question C.

***Question A.***

Créez une classe `Bibliothèque`. Cette classe doit posséder les attributs et méthodes suivants :

- Une méthode `__init__` pour initialiser les attributs suivants :
  - `livres` : un dictionnaire où la clé est le titre du livre et la valeur est le nombre de copies disponibles.
  - `emprunts` : un dictionnaire où la clé est le titre du livre et la valeur est le nombre de copies actuellement empruntées.

- Une méthode `ajouter_livre` pour ajouter des livres à la bibliothèque. Cette méthode prend en paramètres le titre du livre et le nombre de copies. Si le livre existe déjà, augmentez le nombre de copies disponibles.

- Une méthode `emprunter_livre` pour emprunter un livre. Cette méthode prend en paramètres le titre du livre. Si le livre est disponible, diminuez le nombre de copies disponibles et augmentez le nombre de copies empruntées. Si le livre n'est pas disponible, levez une exception de type `ValueError` avec le message : `"Le livre n'est pas disponible"`.

***Question B.***

Ajoutez une méthode `retourner_livre` qui permet de retourner un livre emprunté. Cette méthode prend en paramètres le titre du livre. Augmentez le nombre de copies disponibles et diminuez le nombre de copies empruntées. Si le livre n'a pas été emprunté, levez une exception de type `ValueError` avec le message : `"Le livre n'a pas été emprunté"`.

***Question C.***

Implémentez une méthode `__str__` pour afficher l'état actuel de la bibliothèque. Cette méthode doit retourner une chaîne de caractères listant tous les livres, le nombre de copies disponibles et empruntées pour chaque livre.

### Rendu de l'étudiant :

```python
class bibliotheque:
    def __init__(self):
        self.livres = []
        emprunts = []

    def ajouter_livre(self, titre, nombre):
        if titre in self.livres:
            self.livres[titre] += nombre
        else:
            self.livres[titre] = nombre
            self.emprunts[titre] = 0

    def emprunter_livre(self, titre):
        if self.livres[titre] > 0:
            self.livres[titre] -= 1
            self.emprunts += 1
        else:
            raise ValueError("Le livre n'est pas disponible")

    def retourner_livre(self, titre):
        if self.emprunts[titre] < 0:
            self.livres[titre] += 1
            self.emprunts -= 1
        else:
            raise ValueError("Le livre n'a pas été emprunté")

    def __str__(self):
        print("État de la bibliothèque:")
        for titre in self.livres:
            print(f"{titre} - Disponibles: {self.livres[titre]}, Empruntés: {self.emprunts[titre]")
        return True


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



```

Votre mission est d'identifier et de corriger les erreurs dans la classe `bibliotheque`. Noter que certaines erreurs peuvent être subtiles et concerner les bonnes pratiques de programmation en Python.