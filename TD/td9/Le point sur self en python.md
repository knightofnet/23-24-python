# Le point sur `self` en python

## Qu'est-ce que `self` ?

1. **Identifiant d'instance :** `self` fait référence à l'instance de la classe sur laquelle la méthode est appelée. Autrement dit, il permet d'accéder aux attributs et méthodes de cette instance spécifique.

2. **Similaire à "this" dans d'autres langages :** Si vous êtes familiarisé avec d'autres langages de programmation orientée objet comme Java ou C++, `self` est équivalent à `this`.

## Pourquoi utiliser `self` ?

1. **Accéder aux attributs de l'instance :** `self` permet de distinguer entre les attributs de l'instance (particuliers à chaque objet créé à partir de la classe) et les variables locales à la méthode. Par exemple, `self.nom` se réfère à l'attribut `nom` de l'instance de la classe.

2. **Appeler d'autres méthodes de l'instance :** Vous pouvez utiliser `self` pour appeler d'autres méthodes de la même instance. Par exemple, `self.ma_methode()` appelle la méthode `ma_methode` de cette instance.

## Comment l'utilise-t-on ?

1. **Définir une méthode :** Lorsque vous définissez une méthode dans une classe, vous devez ajouter `self` comme premier paramètre. Cependant, vous ne le passez pas lorsque vous appelez la méthode. Python le fait automatiquement pour vous.

   ```python
   class MaClasse:
       def ma_methode(self):
           print("Un exemple de méthode")
   ```

2. **Créer et utiliser une instance :**

   ```python
   mon_objet = MaClasse()
   mon_objet.ma_methode()  # Pas besoin de passer 'self' ici.
   ```

## À noter :

- **Uniquement pour les méthodes d'instance :** `self` n'est utilisé que pour les méthodes liées à une instance. Les méthodes statiques et de classe n'utilisent pas `self`.
