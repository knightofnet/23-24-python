Bien sûr, voici un exercice similaire qui utilise les mêmes concepts que l'exercice précédent, mais avec un scénario différent :

**Exercice Python : Gestion des Étudiants**

On s'intéresse à la gestion des étudiants d'une école.
1. (3 points : 1 point initialisation, 1 point affichage, 1 point création d'instances)
   On considère une classe `Etudiant` avec les attributs suivants :
   - nom (chaîne de caractères)
   - numéro d'étudiant (entier)
   - moyenne (nombre à virgule flottante)
   
   Créez une méthode d'initialisation pour la classe `Etudiant` qui prend ces attributs en paramètres. Ensuite, ajoutez une méthode `affiche` qui affiche les attributs sous la forme suivante pour une instance `Etudiant("Alice", 12345, 17.5)` :
   ```
   Étudiant : Alice
   Numéro d'étudiant : 12345
   Moyenne : 17.5
   ```

   Créez deux instances d'étudiants avec des données différentes et affichez-les.

2. (4 points : 1 point méthode statique, 1.5 points mise à jour de la moyenne, 1.5 points tests)
   Ajoutez une méthode statique `mention` qui prend en paramètre une moyenne et retourne une mention en fonction de la moyenne de l'étudiant :
   - Si la moyenne est supérieure ou égale à 16, retournez "Très bien".
   - Si la moyenne est entre 14 et 16 (inclus), retournez "Bien".
   - Si la moyenne est entre 12 et 14 (inclus), retournez "Assez bien".
   - Si la moyenne est inférieure à 12, retournez "Insuffisant".
   
   Ensuite, ajoutez une méthode `miseAJourMoyenne` qui permet de mettre à jour la moyenne de l'étudiant en fonction de nouvelles notes (une liste de nombres à virgule flottante). La nouvelle moyenne est calculée en prenant la moyenne des nouvelles notes et des notes précédentes. N'oubliez pas de mettre à jour l'attribut `moyenne` de l'étudiant.

   Testez la méthode `mention` avec différentes moyennes et la méthode `miseAJourMoyenne` avec de nouvelles notes pour un étudiant.

3. (3 points : 1.5 points attribut de classe, 1 point initialisation, 0.5 points suppression d'étudiant)
   Ajoutez un attribut de classe `listeEtudiants` qui sera une liste vide au départ. Modifiez la méthode d'initialisation pour ajouter chaque nouvelle instance `Etudiant` créée à cette liste.

   Ensuite, ajoutez une méthode `supprimerEtudiant` qui prend en paramètre un numéro d'étudiant et supprime l'étudiant correspondant de la liste `listeEtudiants`.

   Testez la création d'étudiants, l'ajout à la liste, et la suppression d'un étudiant par son numéro d'étudiant.

4. (2.5 points : 1 point initialisation, 1 point fonction affiche, 0.5 point création d'instances)
   Créez une sous-classe `EtudiantBoursier` de la classe `Etudiant` avec un attribut supplémentaire `bourse` (booléen) pour indiquer si l'étudiant a une bourse ou non. Modifiez la méthode d'initialisation pour prendre en compte cet attribut.

   Ajoutez une méthode `affiche` dans la sous-classe `EtudiantBoursier` qui affiche tous les attributs, y compris l'information sur la bourse, de la manière suivante pour une instance `EtudiantBoursier("Bob", 54321, 15.0, True)` :
   ```
   Étudiant : Bob
   Numéro d'étudiant : 54321
   Moyenne : 15.0
   Bourse : Oui
   ```

   Créez une instance d'étudiant boursier et affichez-la.

Cet exercice permet de travailler sur la création de classes, l'héritage, les méthodes statiques, la gestion des listes d'instances et la manipulation d'attributs de classe.