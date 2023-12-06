# Exercice : Gestion de Bibliothèque

**Question 1 :**  
Créez une classe `Livre` avec les éléments suivants :

- Un attribut `titre` pour le titre du livre.
- Un attribut `auteur` pour le nom de l'auteur.
- Un attribut `isbn` pour le numéro ISBN du livre.
- Surchargez la méthode `__str__` pour permettre l'affichage des informations d'une instance de Livre.

Testez votre classe en créant plusieurs instances de `Livre`.

**Question 2 :**  

Créez une méthode statique `verifISBN` qui prend en paramètre une chaîne de caractères représentant un numéro ISBN-10 et retourne un booléen. Cette fonction vérifie que la chaîne est un ISBN-10 valide selon les critères suivants :

- Elle doit avoir une longueur de 10 caractères.
- Tous les caractères, sauf le dernier, doivent être des chiffres.
- Le dernier caractère peut être un chiffre ou 'X', qui représente 10.
- Utilisez la formule de vérification ISBN-10 : la somme des produits des dix chiffres par leur position (1 pour le premier chiffre, 2 pour le second, etc.) doit être un multiple de 11.

Dans le constructeur de la classe `Livre`, utilisez cette méthode pour valider le numéro ISBN. Si le numéro n'est pas valide, levez une exception `ValueError`.

**Question 4 :**  
Définissez une classe `Bibliotheque` avec les éléments suivants :

- Un attribut `nom` pour le nom de la bibliothèque.
- Un attribut `livres` initialisé à un dictionnaire vide, où les clés sont les ISBN et les valeurs sont des instances de `Livre`.
- Une méthode `ajouter_livre` pour ajouter un livre à la bibliothèque.
- Une méthode `rechercher_livre` pour trouver un livre par son ISBN.

Testez ces méthodes avec des exemples concrets.

**Question 5 :**  
Ajoutez une méthode `liste_livres` à la classe `Bibliotheque` pour afficher tous les livres de la bibliothèque, triés par auteur ou titre (selon un paramètre).
