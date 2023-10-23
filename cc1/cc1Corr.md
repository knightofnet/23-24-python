# Correction CC1

- [Correction CC1](#correction-cc1)
  - [Exercice 1](#exercice-1)
    - [Question 1](#question-1)
    - [Question 2a](#question-2a)
    - [Question 2b](#question-2b)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
      - [Solution 1 - Parcourir les indices](#solution-1---parcourir-les-indices)
      - [Solution 2 - Utiliser `enumerate()`](#solution-2---utiliser-enumerate)
      - [Solution 3 - Utiliser un compteur externe à la boucle](#solution-3---utiliser-un-compteur-externe-à-la-boucle)
  - [Exercice 2](#exercice-2)
    - [Question 1](#question-1-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3-1)
    - [Question 4](#question-4-1)
      - [Fonction question4()](#fonction-question4)
      - [Fonction compareAnnees()](#fonction-compareannees)
  - [Correction rapide](#correction-rapide)

## Exercice 1

Voici le texte corrigé :

### Question 1

**Énoncé :**

Codez une fonction calculant le nombre d'entiers compris entre 1 et `n`, qui sont divisibles par 8 et non par 6. La fonction demande `n` à l'utilisateur.

**Corrigé :**

Il faut créer une fonction qui compte les multiples de 8 qui ne sont pas des multiples de 6 entre 1 et `n`. En accumulant ces multiples, nous pourrons déterminer leur nombre.

Dans un premier temps, demandons la valeur de `n` à l'utilisateur. Il est précisé que la fonction doit demander `n`, donc l'appel à `input()` doit être fait dans le corps de la fonction. Comme `n` doit être un entier et que la fonction `input()` renvoie une chaîne de caractères, nous devons convertir le retour de `input()` en entier avec `int()`.

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
```

Pour être complet, nous pourrions vérifier que `n` est supérieur à 1, sinon la suite ne fonctionnera pas. Cette vérification n'est pas notée pour le contrôle continu 1 (CC1).

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
```

Ensuite, nous pouvons commencer à compter. Juste avant cela, initialisons une variable qui servira de compteur pour les multiples de 8 qui ne sont pas multiples de 6.

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
    # Initialiser une variable pour compter les multiples
    compteur = 0
```

Nous utiliserons une boucle `for` pour tester chaque entier de 1 à `n`. Une boucle `for` est plus appropriée ici, car nous savons quand il faut s'arrêter.

Attention : nous allons jusqu'à `n`. La borne supérieure de la fonction `range()` est exclue, donc nous devons aller jusqu'à `n + 1`.

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
    # Initialiser une variable pour compter les multiples
    compteur = 0

    for i in range(1, n + 1):
        pass
```

À chaque itération (à chaque tour de boucle), nous effectuerons un test pour déterminer :

- Si `i` est un multiple de 8
- ET si `i` n'est pas un multiple de 6

Pour cela, nous utiliserons l'opérateur modulo (`%` en Python) qui renvoie le reste d'une division euclidienne.

Si `i % 8 == 0`, alors nous saurons que `i` est un multiple de 8. La même logique s'applique pour la condition suivante : nous devons tester que `i % 6 != 0` pour déterminer que `i` n'est pas un multiple de 6.

Nous combinons ces deux conditions avec l'opérateur ET (`and`) pour nous assurer que les deux conditions sont respectées en même temps.

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
    # Initialiser une variable pour compter les multiples
    compteur = 0

    for i in range(1, n + 1):
        # Tester si i est un multiple de 8 et non de 6
        if i % 8 == 0 and i % 6 != 0:
```

Une fois que nous trouvons une valeur valide pour `i`, nous incrémentons le compteur.

Nous renvoyons ensuite ce compteur en fin de fonction.

```python
def cptEnt():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
    # Initialiser une variable pour compter les multiples
    compteur = 0

    for i in range(1, n + 1):
        # Tester si i est un multiple de 8 et non de 6
        if i % 8 == 0 and i % 6 != 0:
            compteur += 1

    return compteur
```

Pour tester la fonction, il faut l'appeler dans l'espace global. Pour cela, vous devez écrire le nom de la fonction suivi d'une paire de parenthèses (sans rien à l'intérieur, car la fonction n'a pas de paramètres en entrée).

```python
# Appel de la fonction cptEnt(). La fonction est appelée, puis son résultat est affiché par la fonction print().
print(cptEnt())
```

**Version alternative, avec les compréhensions de liste :**

Il est possible d'utiliser une liste en compréhension pour résoudre cet exercice. L'idée est de construire une liste des multiples de 8 qui ne sont pas multiples de 6, puis de renvoyer le compte des éléments de la liste.

Rappelez-vous que les compréhensions de liste fonctionnent avec trois parties :

```python
[CCCCCC   AAAAAA   BBBBBB]
```

où :

- AAAAAA est la définition de la boucle
- BBBBBB, optionnel, sont les conditions pour lesquelles nous prenons en compte la valeur d'itération
- CCCCCC est l'opération réalisée avant l'ajout dans la boucle.

En reprenant la correction de la méthode par accumulation, nous avons déjà quelques éléments. Nous pouvons donc adapter le code pour construire la compréhension de liste :

```python
def cptEntComprehension():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))

    # Récupérer la liste construite par compréhension
    lst = [i for i in range(1, n + 1) if i % 8 == 0 and i % 6 != 0]
    # La liste lst contient les multiples de 8 qui ne sont pas multiples de 6, de 1 à n.

    # Renvoyer la longueur de la liste
    return len(lst)
```

Une version plus concise serait la suivante :

```python
def cptEntComprehension():
    # Demander n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n <= 1:
        print("n doit être supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))

    # Récupérer la liste construite par compréhension
    return len([i for i in range(1, n + 1) if i % 8 == 0 and i % 6 != 0])
```

### Question 2a

**Enoncé :**

On considère la fonction f, définie sur ]0;+∞[ par f(x)=1/2 (x+2/x)
Définir f en python et testez que f(5) renvoie 2,7.

**Corrigé :**

Nous allons définir la fonction Python `f(x)` en utilisant la définition mathématique donnée.

Nous devons nous assurer que `x` est supérieur à 0, car la fonction est définie pour x > 0.

```python
def f(x):
    if x <= 0:
        print("x doit être supérieur à 0.")
        return None
    
    return 0.5 * (x + 2 / x)
```

Ici, nous avons ajouté une condition pour vérifier si `x` est supérieur à 0. Si ce n'est pas le cas, un message d'erreur est affiché, et la fonction retourne `None`. Il est important de noter que sans cette vérification sur `x`, la fonction Python `f(x)` est définie comme suit :

```python
def f(x):   
    return 0.5 * (x + 2 / x)
```

Pour vérifier que la fonction `f(x)` est correctement définie, nous proposons de tester si `f(5)` renvoie bien 2.7.

Pour ce faire, deux méthodes sont acceptées :

```python
# Utilisation d'un print()
print("f(5) doit renvoyer 2.7 :", f(5))

# Utilisation d'une assertion
assert f(5) == 2.7
```

### Question 2b

**Enoncé :**

Soit la suite suivante : 𝑎0 > 0, ∀𝑛∈ℕ, 𝑎𝑛+1=𝑓(𝑎𝑛)

En créant une fonction, testez l’évolution de cette suite. Vers quoi semble tendre 𝑎𝑛 pour 𝑛→+∞ ?

**Corrigé :**

Ici, il fallait transposer la suite mathématique de l'énoncé en une fonction Python tout en faisant évoluer la suite sur un intervalle intéressant, par exemple de 1 à 100, de 1 à 1000, ou de 1 à n.

Commençons par définir une fonction, que nous appellerons `evolution_suite`, qui prendra en paramètres :

- un nombre initial `a0` (qui doit être supérieur à 0),
- un nombre d'itérations `n` pour observer l'évolution de la suite.

Nous utiliserons la fonction `f(x)` définie précédemment pour calculer chaque terme suivant de la suite.

La signature de la fonction serait la suivante :

```python
def evolution_suite(a0, n):
    pass
```

Le paramètre `a0` permettra de donner la valeur initiale à la variable `a`, qui contiendra la valeur du terme à chaque itération. Nous utiliserons une boucle `for` pour calculer chaque terme suivant de la suite en utilisant la fonction `f(x)`, puis nous l'afficherons à chaque itération.

```python
def evolution_suite(a0, n):
    a = a0
    for i in range(1, n + 1):
        a = f(a)
        print("Terme a_", i, ":", a)
```

Nous ajoutons un `print()` pour afficher l'évolution de `a`.

Pour utiliser cette fonction, nous pouvons l'appeler avec une valeur de `a0` supérieure à 0, par exemple 1, et un `n` intéressant, par exemple 100. Si `n` n'est pas suffisamment grand pour bien observer l'évolution de la suite, nous pouvons prendre une valeur plus grande.

```python
evolution_suite(1, 100)
```

Remarque : Il ne faut pas écrire `print(evolution_suite(1, 100))`, car la fonction `evolution_suite()` ne renvoie rien, donc il n'y a rien à afficher avec `print()`.

### Question 3

**Enoncé :**

Ecrivez une fonction d’affichage nommée ``afficheChaineBin(texte)`` qui prend en entrée une chaine de caractère et qui affiche caractère par caractère, sur 1 ligne :

- Le caractère,
- Sa représentation décimale puis binaire.

Reproduisez l’affichage ci-dessous.

*Exemple ici si ``texte`` est valorisé avec la chaine de caractère : ``"Test"``*

```shell
T : 84 - 0b1010100
e : 101 - 0b1100101
s : 115 - 0b1110011 
t : 116 - 0b1110100
```

**Corrigé :**

Pour commencer, il faut définir la fonction Python. Voici sa signature (la définition) :

```python
def afficheChaineBin(texte):
    pass
```

On récupère une chaîne de caractères dans la variable `texte`. Pour travailler caractère par caractère, nous pouvons utiliser une boucle `for`. En effet, si nous bouclons sur une chaîne de caractères, à chaque itération, la variable d'itération `c` contiendra un caractère spécifique de la chaîne.

Ce qui donne :

```python
def afficheChaineBin(texte):

    # On itère sur la variable texte.
    # La variable d'itération c prend successivement 
    # le caractère suivant de la chaîne de caractères 
    # contenue dans texte.
    for c in texte:
        pass
```

Maintenant, nous avons un caractère dans `c`. C'est avec ce caractère que nous allons réaliser l'affichage demandé, à savoir :

1. Afficher le caractère.
2. Afficher sa représentation décimale.
3. Afficher sa représentation binaire.

Pour le point 2, pour convertir le caractère en sa valeur décimale, nous utiliserons la fonction `ord()` qui renvoie le nombre entier représentant le code Unicode du caractère donné.

Pour le point 3, nous devons convertir la valeur décimale en binaire. Cependant, plutôt que de rappeler la fonction `ord()`, nous optimiserons le processus en stockant la valeur décimale dans une variable dès le départ. Ensuite, nous utiliserons cette valeur stockée pour obtenir la représentation binaire du caractère.

Enfin, pour afficher le tout, nous pouvons utiliser un seul `print()`.

```python
def afficheChaineBin(texte):

    # On itère sur la variable texte.
    # La variable d'itération c prend successivement 
    # le caractère suivant de la chaîne de caractères 
    # contenue dans texte.
    for c in texte:
        # Point 1 : Nous affichons le caractère avec print. 
        # Pour éviter le retour à la ligne, nous changeons la 
        # valeur du paramètre end de print().
        print(c, ": ", end="")

        # Point 2 : Nous calculons la représentation décimale
        # de c. Nous la stockons dans la variable d.
        d = ord(c)

        # Puis nous l'affichons :
        print(d, "-", end="")

        # Point 3 : Nous affichons la représentation binaire en
        # utilisant la fonction bin() sur d. Cela peut être
        # directement réalisé dans le print().
        # C'est le dernier print(), donc là, il faut qu'il y ait
        # un retour à la ligne à la fin (comportement par défaut
        # de print(), donc nous ne redéfinissons pas le paramètre end.
        print(bin(d))
```

Et voilà ! Maintenant, il faut tester que l'affichage avec `texte="Test"` correspond à celui présenté dans l'énoncé. Pour cela, nous devons appeler la fonction :

```python
afficheChaineBin("Test")
```

Nous pouvons également simplifier la fonction en utilisant un seul `print()`. Voici la version simplifiée :

```python
def afficheChaineBin_alternative(texte):

    # On itère sur la variable texte.
    # La variable d'itération c prend successivement 
    # le caractère suivant de la chaîne de caractères 
    # contenue dans texte.
    for c in texte:
        d = ord(c)
        print(c, ":", d, "-", bin(d))

afficheChaineBin_alternative("Test")
```

Une autre alternative consiste à utiliser le formatage de texte (vu dans le cours 6 sur les chaînes de caractères) :

```python
def afficheChaineBin_alternativeFormat(texte):

    # On itère sur la variable texte.
    # La variable d'itération c prend successivement 
    # le caractère suivant de la chaîne de caractères 
    # contenue dans texte.
    for c in texte:
        d = ord(c)
        print("{} : {} - {}".format(c, d, bin(d)))

afficheChaineBin_alternativeFormat("Test")
```

### Question 4

**Enoncé :**

[Bonus] Ecrivez une fonction ``afficheHisto(lst, car)`` qui prend en entier une liste de réels positifs ou nuls ``lst`` ainsi qu’un paramètre optionnel ``car`` qui est une chaine de caractère. La fonction affiche les valeurs sous la forme d'un histogramme.

Exemple :

```python
lst = [2.5, 5.0, 10.2, 3.4, 6.0] 
afficheHisto(lst)
```

Cela affichera :

```shell
1 : **
2 : *****
3 : **********
4 : ***
5 : ******
```

Le caractère utilisé pour représenter les unités est l’astérisque ``'*'`` par défaut, si le paramètre ``car`` de la fonction n’est pas valorisé. Le cas contraire, la valeur de ``car`` sera utilisée.

Exemple :

```python
afficheHisto(lst, "=")
```

Cela affichera :

```shell
1 : ==
2 : =====
3 : ==========
4 : ===
5 : ======
```

**Corrigé :**

Pour répondre à cette question, il faut d'abord comprendre et examiner attentivement toutes les indications données.

Il s'agit de créer une fonction Python nommée `afficheHisto(lst, car)` avec deux paramètres : `lst` et `car`. En examinant l'exemple fourni, on peut voir que l'histogramme dépend des valeurs de `lst`. Cependant, dans `lst`, nous avons des nombres décimaux, mais l'histogramme est basé sur la valeur entière de chaque élément.

Commençons par définir la fonction :

```python
def afficheHisto(lst, car) :
    pass
```

Nous savons que `car` est un paramètre optionnel avec une valeur par défaut de `'*'`.
La signature de la fonction devient alors :

```python
def afficheHisto(lst, car="*") :
    pass
```

Nous pourrions directement boucler sur `lst` de la manière suivante :

```python
for elt in lst:
    pass  # À cet endroit, nous effectuerons des opérations sur 'elt'
```

À ce stade, `elt` contient successivement un élément de `lst`. Cependant, si nous examinons l'affichage souhaité, nous constatons que chaque ligne commence par l'indice de l'élément (à partir de 1). Nous avons donc besoin d'un moyen d'obtenir cet indice. Il existe plusieurs façons de le faire :

- Solution 1 : changer la définition de la boucle pour parcourir les indices plutôt que les éléments de `lst`.
- Solution 2 : utiliser `enumerate(lst)` pour obtenir un tuple contenant deux valeurs : l'indice de l'élément et la valeur de l'élément.
- Solution 3 : ajouter un compteur que nous incrémenterons à chaque itération.

La solution 2 semble être la plus concise. Cependant, examinons également les autres options :

#### Solution 1 - Parcourir les indices

Nous pouvons changer la manière dont nous bouclons en utilisant les indices pour accéder aux éléments de la liste. Cette approche peut être utile lorsque l'indice lui-même est nécessaire pour effectuer des opérations supplémentaires ou pour l'affichage.

Pour cela, nous bouclerions sur une plage d'indices, de 0 à l'indice du dernier élément (soit `len(lst) - 1`). En Python, nous pouvons utiliser `range()`. Comme la borne supérieure est exclue avec `range()`, nous ajoutons +1 pour l'inclure, ce qui donne :

```python
range(0, len(lst) - 1 + 1)
```

Ce qui équivaut à :

```python
range(0, len(lst))
```

Ou encore plus simplement :

```python
range(len(lst))
```

Pour notre fonction, cela donnerait :

```python
def afficheHisto(lst, car="*"):
    for i in range(len(lst)):
        pass
```

À ce stade, nous avons `i` qui commence à 0. Nous pourrions utiliser une variable `j` pour avoir `i + 1` comme valeur et ainsi obtenir une numérotation commençant à 1.

Avec `i`, on peut également récupérer la valeur d'élément à la position `i` dans la liste `lst`.

Ce qui donne :

```python
def afficheHisto(lst, car="*") :
    for i in range(len(lst)) :
        j = i + 1
        elt = lst[i]
```

À ce stade, nous avons la valeur à afficher contenue dans la variable `elt`. Cependant, pour procéder à l'affichage, il est nécessaire de convertir cette valeur en un entier. Cette étape est indispensable car elle garantit que la multiplication de chaînes par un entier se déroule sans encombre.

En l'état actuel, utiliser `elt` directement pour la multiplication des chaînes pourrait s'avérer problématique. Cela est dû au fait que `elt` pourrait potentiellement être un nombre réel. Dans un tel scénario, la multiplication de chaînes par un nombre réel pourrait entraîner une erreur ou un comportement imprévu, car Python s'attend à un opérande entier pour cette opération.

Pour convertir elt en entier, on utilise la fonction `int()`.

Ensuite, il n'y a plus qu'à réaliser l'affichage. Ce qui donne :

```python
def afficheHisto(lst, car="*"):
    for i in range(len(lst)):
        j = i + 1
        elt = lst[i]

        # Affichage en mode histogramme :
        eltEntier = int(elt)
        print(j, ":", car * eltEntier)
```

#### Solution 2 - Utiliser `enumerate()`

Cette solution est plus claire et plus concise. En utilisant simplement la fonction `enumerate()`, nous obtenons à la fois l'indice de l'élément et sa valeur.

Ensuite, la partie d'affichage ne change pas, ce qui donne :

```python
def afficheHisto(lst, car="*"):
    for i, elt in enumerate(lst):
        j = i + 1

        # Affichage en mode histogramme :
        eltEntier = int(elt)
        print(j, ":", car * eltEntier)
```

Notez que la fonction `enumerate()` nous permet également de gérer le début de la numérotation à 1 en spécifiant la valeur de départ avec le paramètre `start`. Nous n'avons donc plus besoin de `i` dans notre fonction :

```python
def afficheHisto(lst, car="*"):
    for j, elt in enumerate(lst, start=1):
        # Affichage en mode histogramme :
        eltEntier = int(elt)
        print(j, ":", car * eltEntier)
```

#### Solution 3 - Utiliser un compteur externe à la boucle

L'idée ici est de définir et d'incrément

er un compteur. C'est une approche un peu plus manuelle, mais elle peut être utile dans certains contextes. Voici comment cela fonctionne :

```python
def afficheHisto(lst, car="*"):
    # Nous initialisons le compteur à 1, car la numérotation commence à 1 dans notre exercice.
    j = 1

    # Nous pouvons utiliser la boucle for directement sur la liste
    # et obtenir directement 'elt'.
    for elt in lst:

        # Affichage en mode histogramme :
        eltEntier = int(elt)
        print(j, ":", car * eltEntier)

        # Nous incrémentons le compteur :
        j += 1
```

Choisissez la solution qui vous convient le mieux en fonction de vos besoins.

## Exercice 2

### Question 1

**Enoncé :**

Ecrire une fonction ``genereListeTemperature(nbJour, tMin, tMax)`` avec 3 paramètres en entrée :

- ``nbJour`` : Un entier représentant le nombre de jours pour lesquels générer des températures,
- ``tMin`` : Un nombre réel indiquant la température minimale possible,
- ``tMax`` : Un nombre réel indiquant la température maximale possible

La fonction doit retourner une liste de ``nbJour`` températures aléatoires, chaque température étant un nombre réel choisi aléatoirement entre ``tMin`` et ``tMax``. Chaque température dans la liste doit être arrondie à deux chiffres après la virgule.

*Exemple :*

```python
temperatures = genereListeTemperature(30, 10.5, 25.8) 
print(temperatures)
```

Dans cet exemple, temperatures sera une liste de 30 températures aléatoires, chacune comprise entre 10.5°C et 25.8°C, et arrondie à deux chiffres après la virgule.

Remarque : La fonction ``randint(min, max)`` du module random n'est pas appropriée ici, puisqu'elle retourne un entier. Utilisez à la place la fonction ``uniform(min, max)`` du module random pour tirer aléatoirement un réel entre min et max.

**Corrigé :**

Pour générer un ensemble de valeurs, nous devons suivre les indications fournies à la fin de l'énoncé, qui nous indiquent d'utiliser la fonction `uniform()` du module `random`. Commençons par importer cette fonction :

```python
from random import uniform
```

Ensuite, nous pouvons définir la fonction en écrivant sa signature :

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    pass
```

Puisque la fonction doit retourner une liste de températures, nous commençons le code de la fonction par initialiser une liste vide, `temperatures`, pour stocker les températures que nous allons générer.

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    # Initialisation de la liste pour stocker les températures générées.
    temperatures = []
```

Ensuite, puisque nous savons que nous avons besoin d'un nombre précis de températures, soit `nbJour`, nous utilisons une boucle `for` pour générer ces températures.

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    # Initialisation de la liste pour stocker les températures générées.
    temperatures = []

    for _ in range(nbJour) :
        pass
```

À chaque itération, nous faisons ce qui suit :

- Nous générons une température aléatoire entre `tMin` et `tMax` en utilisant la fonction `uniform()`.
- Ensuite, nous arrondissons cette valeur à deux chiffres après la virgule en utilisant la fonction `round()`.
- Enfin, nous ajoutons cette valeur arrondie à la liste `temperatures`.

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    # Initialisation de la liste pour stocker les températures générées.
    temperatures = []

    for _ in range(nbJour) :
        # Génération d'une température aléatoire entre tMin et tMax
        t = uniform(tMin, tMax)
        # Arrondissement de la température à deux chiffres après la virgule avec la fonction round()
        tArrondie = round(t, 2)
        # Ajout de cette température arrondie à la liste temperatures
        temperatures.append(tArrondie)
```

De manière plus concise, nous pouvons également écrire ceci :

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    # Initialisation de la liste pour stocker les températures générées.
    temperatures = []

    for _ in range(nbJour) :
        temperatures.append(round(uniform(tMin, tMax), 2))
```

Enfin, nous retournons la liste des températures à la fin de la fonction.

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    # Initialisation de la liste pour stocker les températures générées.
    temperatures = []

    for _ in range(nbJour) :
        # Génération d'une température aléatoire entre tMin et tMax
        t = uniform(tMin, tMax)
        # Arrondissement de la température à deux chiffres après la virgule avec la fonction round()
        tArrondie = round(t, 2)
        # Ajout de cette température arrondie à la liste temperatures
        temperatures.append(tArrondie)

    return temperatures
```

**Version alternative avec les compréhensions de listes :**

Il était possible d'utiliser une construction par compréhension pour résoudre cette question de manière plus concise :

```python
from random import uniform

def genereListeTemperature(nbJour, tMin, tMax) :
    return [round(uniform(tMin, tMax), 2) for _ in range(nbJour)]
```

### Question 2

**Enoncé :**

Ecrire une fonction `genereAnnee()`, sans paramètre, qui retourne une liste complète de températures pour chaque d’une année en utilisant les tuples `nbrJoursParMois` et `tParMois` ainsi que la fonction `genereListeTemperature(nbJour, tMin, tMax)` de la question 1.

Ainsi, il y aura dans cette liste 31 mesures de températures générées aléatoirement entre 2°C et 7.8°C pour le mois de janvier, 28 mesures de températures générées aléatoirement entre 4.5°C et 11.8°C pour le mois de février, 31 pour mars, etc.

Dans le corps principal, testez qu'il y ait bien 365 éléments dans la liste en retour, correspondant aux 365 relevés de températures avec le code suivant que vous pourrez placer dans l’espace principal :

```python
temperatures_annee = genereAnnee() 
# La liste devrait contenir 365 éléments. 
assert len(temperatures_annee) == 365 
print("Nombre total de jours :", len(temperatures_annee)) 
print("Températures de l'année :", temperatures_annee)
```

**Corrigé :**

Avec la question 1, nous avons défini une fonction permettant de créer une liste de `nbJour` températures entre deux bornes `tMin` et `tMax`. Dans cette question, nous allons utiliser les deux tuples fournis pour valoriser les paramètres de la fonction `genereListeTemperature(nbJour, tMin, tMax)` de la question 1 afin de construire une liste finale correspondant aux températures d'une année entière.

Commençons par définir la fonction :

```python
def genereAnnee() :
    pass
```

Puisque la fonction doit retourner une liste de températures correspondant à une année entière, nous commençons le code de la fonction en créant une liste vide `temperaturesAn` pour stocker les températures.

```python
def genereAnnee() :
    # Initialisation de la liste pour stocker les températures générées.
    temperaturesAn = []

    for nbJour in nbrJoursParMois :
        pass
```

Il est nécessaire de construire des sous-listes, une par mois. Ensuite, nous ajouterons les éléments de ces sous-listes dans la liste `temperaturesAn`. Puisqu'il faut générer une sous-liste par mois, nous utiliserons une boucle `for`. Mais quelle type de boucle `for` devons-nous utiliser ?

La méthode la plus simple consiste à utiliser les indices. Une boucle avec `enumerate()` simplifierait également les choses. Les deux approches sont appropriées ici, car nous avons besoin :

- du nombre de jours d'un mois, `nbJour`, que nous pouvons trouver comme valeur dans le tuple `nbrJoursParMois`.
- mais aussi de l'indice où nous avons trouvé cet élément, car au même indice, nous trouverons `tMin` et `tMax` dans le tuple `tParMois`.

Ces deux tuples ont été copiés dans l'espace global de votre fichier, ce qui signifie qu'ils sont accessibles dans n'importe quelle fonction en tant que variables globales.

Ce qui donne :

```python
def genereAnnee() :
    # Initialisation de la liste pour stocker les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # Nous récupérons le nombre de jours pour un mois.
        nbJourPourUnMois = nbrJoursParMois[i]

        # Nous récupérons les températures min et max dans le tuple tParMois.
        temperaturesMinEtMax = tParMois[i]

        tpMin = temperaturesMinEtMax[0]
        tpMax = temperaturesMinEtMax[1]
```

Ou en utilisant l'unpacking de tuple :

```python
def genereAnnee() :
    # Initialisation de la liste pour stocker les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # Nous récupérons le nombre de jours pour un mois.
        nbJourPourUnMois = nbrJoursParMois[i]
        # Nous récupérons les températures min et max dans le tuple tParMois.
        tpMin, tpMax = tParMois[i]
```

À ce stade, nous avons trois variables, `nbJourPourUnMois`, `tMin`, et `tMax`, qui nous permettront de valoriser les paramètres de la fonction `genereListeTemperature(nbJour, tMin, tMax)` de la question 1. Nous pouvons donc l'utiliser pour obtenir une sous-liste de `nbJourPourUnMois` températures entre `tpMin` et `tpMax` :

```python
def genereAnnee() :
    # Initialisation de la liste pour stocker les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # Nous récupérons le nombre de jours pour un mois.
        nbJourPourUnMois = nbrJoursParMois[i]
        # Nous récupérons les températures min et max dans le tuple tParMois.
        tpMin, tpMax = tParMois[i]

        # Nous récupérons une liste de températures.
        ssListe = genereListeTemperature(nbJourPourUnMois, tpMin, tpMax)
```

À chaque tour de boucle, nous pouvons étendre la liste finale, `temperaturesAn`, avec cette sous-liste en utilisant la méthode `extend()` de la liste `temperaturesAn` :

```python
def genereAnnee() :
    # Initialisation de la liste pour stocker les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # Nous récupérons le nombre de jours pour un mois.
        nbJourPourUnMois = nbrJoursParMois[i]
        # Nous récupérons les températures min et max dans le tuple tParMois.
        tpMin, tpMax = tParMois[i]

        # Nous récupérons une liste de températures.
        ssListe = genereListeTemperature(nbJourPourUnMois, tpMin, tpMax)

        # Nous étendons la liste finale avec cette sous-liste.
        temperaturesAn.extend(ssListe)

    return temperaturesAn
```

Avec les éléments fournis dans le fichier cc1.py, vous avez tout ce dont vous avez besoin pour tester la fonction :

```python
temperatures_annee = genereAnnee()
# La liste devrait contenir 365 éléments.
assert len(temperatures_annee) == 365
print("Nombre total de jours :", len(temperatures_annee))
print("Températures de l'année :", temperatures_annee)
```

### Question 3

**Enoncé :**

Ecrire une fonction `moyennesAnnee()` qui prend en entrée la liste des 365 relevés de températures (la liste en sortie de la question 2). Cette fonction :

- Réalisera l’affichage suivant :
  
```shell
Moyennes :
 Mois 1 (31 jours) : 4.9 °C 
 Mois 2 (28 jours) : 8.15 °C 
 Mois 3 (31 jours) : 8.7 °C 
 Mois 4 (30 jours) : 10.05 °C 
 Mois 5 (31 jours) : 13.4 °C 
 Mois 6 (30 jours) : 19.55 °C 
 Mois 7 (31 jours) : 20.2 °C 
 Mois 8 (31 jours) : 19.7 °C 
 Mois 9 (30 jours) : 19.0 °C 
 Mois 10 (31 jours) : 13.45 °C 
 Mois 11 (30 jours) : 8.1 °C 
 Mois 12 (31 jours) : 7.05 °C
```

- Retournera une liste de 12 nombres réels, chaque élément représentant la moyenne des températures d’un mois spécifique, arrondi à deux chiffres après la virgule. Utilisez les informations du tuple `nbrJoursParMois`.

*Exemple de liste retournée :*

```python
[4.9, 8.15, 8.7, 10.05, 13.4, 19.55, 20.2, 19.7, 19.0, 13.45, 8.1, 7.05]
```

**Corrigé :**

Commençons par définir la fonction :

```python
def moyennesAnnee(listeAnnee) :
    pass
```

Cette fonction prend en entrée la liste créée à la question 2, et va produire une nouvelle liste, contenant les moyennes des températures par mois.

Puisque la fonction va devoir retourner une liste, on commence le code  de la fonction par initialiser une liste vide ``moyennes`` pour conserver les moyennes par mois des températures.

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []
```

Pour pouvoir faire la moyenne par mois, il va falloir découper en sous-liste de nbJour éléments, la liste en entrée (faire un peu l'inverse de la fonction de la question 2). On sait qu'on a 12 mois, et pour chaque mois, le tuple nbrJoursParMois renseigne le nombre de jour.

On peut alors boucler sur le tuple nbrJoursParMois. Mais là encore, avec quel type de boucle ? On peut boucler sur les indices, ou avec enumerate(). C'est cette solution que l'on va illustrer ici.

A chaque tour de boucle, avec enumerate(), on récupère à la fois l'indice de l'élément et sa valeur.

Ce qui donne :

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    for i, nbrJour in enumerate(nbrJoursParMois) :
        pass
```

L'indice nous permettra de réaliser l'affiche par la suite.

Avec le nombre de jour `nbrJour`, on va pouvoir découper la liste initiale en utilisant le slicing. Il faut un indice de départ et un indice d'arrivé (+1 car il est exclu). 

Pour le 1er mois, c'est facile :

- l'indice de départ, c'est 0
- l'indice d'arrivé, c'est le nombre de jour dans le mois nbrJour.

Sur la liste de départ, cela donne :

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    for i, nbrJour in enumerate(nbrJoursParMois) :
        # ici nbrJour vaut 31
        ssListe = listeAnnee[0:nbrJour]
```

Pour le second mois, on ne peut pas partir de 0, mais nbrJour + 1, puisque le mois de février commence au 32 éléments de `listeAnnee`, donc à l'indice 31 de la liste `listeAnnee`.

Il est donc nécessaire de garder en mémoire (donc dans une variable, par exemple `indiceDebutMois`) la valeur précédente de `nbrJour`, pour avoir la borne de départ. Et pour gérer le mois M+1, il faut mettre à jour cette valeur.

Pour la borne max, il suffira de demander `indiceDebutMois + nbrJour`. On aura ainsi :

Pour janvier, mois 01 :

- borneMin : indiceDebutMois  0 au départ
- borneMax : indiceDebutMois (0) + nbrJour (31) => 31
- indiceDebutMois : incrément de + nbrJour
  
Pour février, mois 02 :

- borneMin : indiceDebutMois  31
- borneMax : indiceDebutMois (31) + nbrJour (28) => 59
- indiceDebutMois : incrément de + nbrJour

Et ainsi de suite.
Ce qui donne :

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # On peut afficher la longueur de ssListe à cette 
        # étape, pour voir si on n'est pas trompé. 
        # La longueur des mois doit s'afficher.
        print(len(ssListe))

moyennesAnnee(temperatures_annee)
```

Une fois qu'on récupère `ssListe` pour chaque tour de boucle, il suffit de calculer la moyenne des températures de cette sous-liste. Puis d'ajouter cette moyenne à la liste de retour : `moyennes`.

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)

        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)
```

Maintenant qu'on a tout ce qu'il nous faut pour la liste en retour de cette fonction, on peut s'occuper de l'affichage.

Pour gérer plus facilement les espaces, on peut valoriser le paramètre sep de print avec une chaine vide (`sep=""`). Le nombre de jour affiché peut être recupéré directement avec `nbrJour` ou alors avec `len(ssListe)`.

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    print("Moyennes :")

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)
        # on arrondi la moyenne avec deux chiffres après la virgule :
        moy = round(moy, 2)

        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)

        # affichage :
        print(" Mois ", i, " (", len(ssListe), " jours) : ", moy," °C", sep="")

moyennesAnnee(temperatures_annee)
```

Si on teste cette étape intermédiaire, on constate un petit souci dans l'affichage :

```shell
Moyennes :
 Mois 0 (31 jours) : 4.77 °C
 Mois 1 (28 jours) : 7.79 °C
 Mois 2 (31 jours) : 8.75 °C
 Mois 3 (30 jours) : 9.46 °C
 Mois 4 (31 jours) : 14.16 °C
 Mois 5 (30 jours) : 20.65 °C
 Mois 6 (31 jours) : 19.49 °C
 Mois 7 (31 jours) : 19.19 °C
 Mois 8 (30 jours) : 19.1 °C
 Mois 9 (31 jours) : 13.12 °C
 Mois 10 (30 jours) : 8.14 °C
 Mois 11 (31 jours) : 7.77 °C
```

La numératation des mois commence à 0, au lieu de 1. Pour corriger cela on peut soit :

- introduire une variable `j` dont la valeur sera `i + 1`.
- écrire `i + 1` dans le `print()`.

On va prendre la seconde option. Pour la première option, reportez vous à la question 1, exercice 4 : c'est la même logique.

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    print("Moyennes :")

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)
        # on arrondi la moyenne avec deux chiffres après la virgule :
        moy = round(moy, 2)

        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)

        # affichage :
        print(" Mois ", i + 1, " (", len(ssListe), " jours) : ", moy," °C", sep="")

moyennesAnnee(temperatures_annee)
```

Cette fois-ci l'affichage est OK. On n'oublie pas d'ajouter le retour de la fonction : elle doit renvoyer la liste des moyennes. Et cette fois c'est terminé :

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    print("Moyennes :")

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Extraction des températures du mois courant :
        # ----
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # Calcul de la moyenne des températures du mois courant :
        # ----
        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)
        # on arrondi la moyenne avec deux chiffres après la virgule :
        moy = round(moy, 2)
        
        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)

        # Affichage de la moyenne :
        # ----
        print(" Mois ", i + 1, " (", len(ssListe), " jours) : ", moy," °C", sep="")

    return moyennes

moyennesAnnee(temperatures_annee)
```

Avec la formatage des chaines, que l'on a vu dans le cours 6, on aurait pu simplifier le print() responsable de l'affichage :

```python
def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    print("Moyennes :")

    for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)
        # on arrondi la moyenne avec deux chiffres après la virgule :
        moy = round(moy, 2)

        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)

        # affichage :
        print(" Mois {} ({} jours) : {} °C".format(i + 1, len(ssListe), moy))

        return moyennes

moyennesAnnee(temperatures_annee)
```

### Question 4

**Enoncé :**

*Question 4.(a)*

Écrivez une fonction `question4()` sans paramètre qui génère deux listes de températures annuelles et leurs moyennes mensuelles. Utilisez les fonctions précédentes.

*Question 4.(b)*

Écrivez une fonction `compareAnnees(listeA, listeB)` qui compare les températures mensuelles moyennes de deux années différentes et renvoie un score basé sur la comparaison. Comparez les éléments correspondants des deux listes. Incrémentez le score de +1 si l'élément de `listeA` est supérieur à celui de `listeB`, et de -1 dans le cas contraire. Enfin, retournez le score final après avoir comparé tous les éléments.

*Question 4.(c)*

Dans le corps de la fonction `question4()`, comparez les deux listes de moyennes puis, si le score renvoyé par `compareAnnees()` est positif, affichez :

```shell
Les températures de la liste A sont en moyennes supérieures à celles de la liste B
```

Sinon affichez :

```shell
Les températures de la liste A sont en moyennes supérieures à celles de la liste B
```

N'oubliez pas d'appeler la fonction `question4()` dans le corps principal de votre fichier.

**Corrigé :**

La question 4 se décompose en 3 sous-parties, mais on va corriger le tout en un seul bloc.

#### Fonction question4()

Au début, on vous propose de créer une fonction question4() qui va avoir le rôle de fonction exécutante pour ce que l'on va faire durant la question... 4 ! Dans cette fonction et en utilisant les fonctions définies précédemment, vous devez générer deux années puis les moyennes de ces deux années.

Ce qui donne :

```python
def question4() :

    # on récupère les éléments (températures et moyennes)
    # pour l'année A
    temperaturesAnneeA = genereAnnee()
    moyennesA = moyennesAnnee(temperaturesAnneeA)

    # on récupère les éléments (températures et moyennes)
    # pour l'année B
    temperaturesAnneeB = genereAnnee()
    moyennesB = moyennesAnnee(temperaturesAnneeB)
```

On n'a pas encore définit la fonctin compareAnnees(), mais on peut déjà préparer son appel et faire le test indiqué dans la question 4.(c). A priori, cette fonction va renvoyer un nombre. Selon que ce nombre soit positif ou négatif, on affichera un message différent. Ce qui donne :

```python
def question4() :

    # on récupère les éléments (températures et moyennes)
    # pour l'année A
    temperaturesAnneeA = genereAnnee()
    moyennesA = moyennesAnnee(temperaturesAnneeA)

    # on récupère les éléments (températures et moyennes)
    # pour l'année B
    temperaturesAnneeB = genereAnnee()
    moyennesB = moyennesAnnee(temperaturesAnneeB)

    scoreComparaison = compareAnnees()
    if (scoreComparaison > 0) :
        print("Les températures de la liste A sont en moyennes supérieures à celles de la liste B")
    else :
        print("Les températures de la liste B sont en moyennes supérieures à celles de la liste A")
```

Il ne reste plus qu'à implémenter la fonction compareAnnees().

#### Fonction compareAnnees()

Cette fonction va renvoyer un score de comparaison entre deux années, représentées par deux listes passées en paramètres. On peut commencer par écrire la définition de la fonction :

```python
def compareAnnees(lstA, lstB) :
    pass
```

On va comparer deux à deux, les éléments de listes `lstA` et `lstB`. Pour chaque comparaison, si l'élément de `lstA` est supérieur à celui de `lstB`, alors on ajoutera 1 au score final, sinon on retranchera 1. Pour que cela puisse fonctionner correctement, on pourrait tester que les deux listes `lstA` et `lstB` aient la même longueur :

```python
def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None    
```

La fonction retourne un score final. On va initialiser ce score à 0 pour commencer :

```python
def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 
```

On va parcourir les listes en bouclant sur les indices (de l'une ou de l'autre, peut importe vu qu'on sait qu'elles ont le même nombre d'éléments). Pour cela, une boucle for sur les indices est recommandée, car on devoir récupérer l'élément de la liste `lstA` à la position `i`, mais également celui de la liste `lstB` à la position `i` afin de procéder à la comparaison :

```python
def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 

    for i in range(len(lstA)) :
        # on récupère les éléments :
        eltA = lstA[i]
        eltB = lstB[i]

        # on effectue la comparaison de eltA et eltB, et 
        # met à jour le scoreFinal en conséquence :
        if eltA > eltB :
            scoreFinal += 1
        else :
            scoreFinal -= 1
```

Une fois que l'on a comparé tous les éléments, on peut renvoyer le score final :

```python
def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 

    for i in range(len(lstA)) :
        # on récupère les éléments :
        eltA = lstA[i]
        eltB = lstB[i]

        # on effectue la comparaison de eltA et eltB, et 
        # met à jour le scoreFinal en conséquence :
        if eltA > eltB :
            scoreFinal += 1
        else :
            scoreFinal -= 1

    return scoreFinal
```

Et voilà ! Maintenant on mets tout ensemble, et on n'oublie pas l'appel de la fonction `question4()` :

```python
def question4() :

    # on récupère les éléments (températures et moyennes)
    # pour l'année A
    temperaturesAnneeA = genereAnnee()
    moyennesA = moyennesAnnee(temperaturesAnneeA)

    # on récupère les éléments (températures et moyennes)
    # pour l'année B
    temperaturesAnneeB = genereAnnee()
    moyennesB = moyennesAnnee(temperaturesAnneeB)

    scoreComparaison = compareAnnees()
    if (scoreComparaison > 0) :
        print("Les températures de la liste A sont en moyennes supérieures à celles de la liste B")
    else :
        print("Les températures de la liste B sont en moyennes supérieures à celles de la liste A")

def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 

    for i in range(len(lstA)) :
        # on récupère les éléments :
        eltA = lstA[i]
        eltB = lstB[i]

        # on effectue la comparaison de eltA et eltB, et 
        # met à jour le scoreFinal en conséquence :
        if eltA > eltB :
            scoreFinal += 1
        else :
            scoreFinal -= 1

    return scoreFinal

question4()
```

**Version alternative pour compareAnnees(), hors programme**

Pour la fonction `compareAnnees()`, on pouvait simplifier la boucle en utilisant une fonction que l'on ne voit pas cette année : la fonction `zip(lstA, lstB, ...)`.

La fonction `zip()` prend comme argument deux ou plusieurs listes (ou autres itérables) et retourne un itérateur de tuples, où le premier élément de chaque itérable passé est associé ensemble, puis le deuxième élément de chaque itérable passé est associé ensemble, et ainsi de suite.

Si les itérables passés à `zip()` sont de longueurs différentes, `zip()` s'arrête dès que le plus court des itérables est épuisé.

Ce qui aurait donné :

```python
def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 

    for eltA, eltB in zip(lstA, lstB) :
        # on effectue la comparaison de eltA et eltB, et 
        # met à jour le scoreFinal en conséquence :
        if eltA > eltB :
            scoreFinal += 1
        else :
            scoreFinal -= 1

    return scoreFinal
```

Toujours hors-programme, et pour en écrire toujours moins, la même fonction pouvait etre écrite comme cela (en retirant la vérificaiton de longueur) :

```python
def compareAnnees(lstA, lstB):
    return sum(1 if eltA > eltB else -1   for eltA, eltB in zip(lstA, lstB))
```

## Correction rapide

```python
###################################################
# Contrôle Continue 1 – Algorithmique avec Python #
###################################################

# Good Luck !

# Exercice 1
# ===========

# Question 1
# ----------

def cptEnt() :
    # on demande n à l'utilisateur
    n = int(input("Entrez une valeur pour n :"))
    while n<= 1 :
        print("n doit etre supérieur à 1 !")
        n = int(input("Entrez une valeur pour n :"))
    
    # on initialise une variable qui servira à compter les multiples par la suite
    compteur = 0

    for i in range(1, n + 1) :
        # on teste que i soit multiple de 8 et pas de 6
        if i % 8 == 0 and i % 6 != 0 :
            compteur += 1

    return compteur

# Appel de la fonction cptEnt(). La fonction est appelée, puis son résultat est affiché par la fonction print().
print(cptEnt())


# Question 2a
# ----------

def f(x):   
    return 0.5 * (x + 2/x)

# Test avec un print()
print("f(5) doit donner 2.7", f(5))
# Test avec une assertion
assert f(5) == 2.7


# Question 2b
# ----------

def evolution_suite(a0, n) :  
    a = a0
    for i in range(1,n) :
        a = f(a)
        print("Terme a_", i,":",a)

evolution_suite(1, 1000)
# a_n tends vers 1.41, vers racine de 2.


# Question 3
# ----------

def afficheChaineBin(texte) :

    # On itère sur la variable texte.
    # La variable d'itération c prend successivement 
    # le caractère suivant de la chaine de caractères 
    # contenu dans texte.
    for c in texte :
        d = ord(c)        
        print(c, ":", d, "-", bin(d))

afficheChaineBin("Test")


# Question 4 - BONUS
# ----------

def afficheHisto(lst, car="*") :
    for i in range(len(lst)) :
        j = i + 1
        elt = lst[i]

        # affichage en mode histogramme :
        eltEntier = int(elt)
        print(j, ":", car * eltEntier)

lst = [2.5, 5.0, 10.2, 3.4, 6.0]
afficheMoyennes(lst)

lst = [2.5, 5.0, 10.2, 3.4, 6.0]
afficheMoyennes(lst, '=')


# Exercice 2
# ===========

# Tuple indiquant le nombre de jours dans chaque mois
nbrJoursParMois = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# Tuple contenant les tuples des températures minimales et maximales observées chaque mois.
tParMois = ( 
    (2, 7.8), 
    (4.5, 11.8), 
    (3.7, 13.7), 
    (4.7, 15.4), 
    (8.7, 18.1), 
    (14.6, 24.5), 
    (15.5, 24.9), 
    (14.8, 24.6), 
    (14, 24), 
    (8.6, 18.3), 
    (4.9, 11.3), 
    (3.8, 10.3)
)

# Question 1
# ----------

def genereAnnee() :
    # on initialise la liste qui gardera les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # on recupère le nombre de jour pour un mois
        nbrJourPourUnMois = nbrJoursParMois[i]
        # on récupère les températures min et max, 
        # dans le tuple tParMois.
        tpMin, tpMax = tParMois[i]

        # on recupère une liste de températures
        ssListe = genereListeTemperature(nbrJourPourUnMois, tpMin, tpMax)

        temperaturesAn.extend(ssListe)

    return temperaturesAn

temperatures_annee = genereAnnee()
# La liste devrait contenir 365 éléments.
assert len(temperatures_annee) == 365
print("Nombre total de jours :", len(temperatures_annee))
print("Températures de l'année :", temperatures_annee)


# Question 2
# ----------

def genereAnnee() :
    # on initialise la liste qui gardera les températures générées.
    temperaturesAn = []

    for i in range(len(nbrJoursParMois)) :
        # on recupère le nombre de jour pour un mois
        nbrJourPourUnMois = nbrJoursParMois[i]
        # on récupère les températures min et max, 
        # dans le tuple tParMois.
        tpMin, tpMax = tParMois[i]

        # on recupère une liste de températures
        ssListe = genereListeTemperature(nbrJourPourUnMois, tpMin, tpMax)

        temperaturesAn.extend(ssListe)

    return temperaturesAn

temperatures_annee = genereAnnee()
# La liste devrait contenir 365 éléments.
assert len(temperatures_annee) == 365
print("Nombre total de jours :", len(temperatures_annee))
print("Températures de l'année :", temperatures_annee)


# Question 3
# ----------

def moyennesAnnee(listeAnnee) :
    moyennes = []

    # On définit l'indice de départ, la borneMin du range.
    # Au départ, à 0
    indiceDebutMois = 0

    print("Moyennes :")

     for i, nbrJour in enumerate(nbrJoursParMois) :
        
        # Extraction des températures du mois courant :
        # ----
        # Sous liste récupérant les éléments d'un mois.
        ssListe = listeAnnee[indiceDebutMois : indiceDebutMois + nbrJour]
        # Mise à jour de l'indice de départ
        indiceDebutMois += nbrJour

        # Calcul de la moyenne des températures du mois courant :
        # ----
        # on calcule la moyenne : la somme des éléments de
        # ssListe divisée par la longeur de ssListe.
        moy = sum(ssListe) / len(ssListe)
        # on arrondi la moyenne avec deux chiffres après la virgule :
        moy = round(moy, 2)
        
        # on ajoute notre moyenne calculée, moy, à la liste
        # de retour : moyennes.
        moyennes.append(moy)

        # Affichage de la moyenne :
        # ----
        print(" Mois ", i + 1, " (", len(ssListe), " jours) : ", moy," °C", sep="")

    return moyennes


# Question 4
# ----------

def question4() :

    # on récupère les éléments (températures et moyennes)
    # pour l'année A
    temperaturesAnneeA = genereAnnee()
    moyennesA = moyennesAnnee(temperaturesAnneeA)

    # on récupère les éléments (températures et moyennes)
    # pour l'année B
    temperaturesAnneeB = genereAnnee()
    moyennesB = moyennesAnnee(temperaturesAnneeB)

    scoreComparaison = compareAnnees(moyennesA, moyennesB)
    if (scoreComparaison > 0) :
        print("Les températures de la liste A sont en moyennes supérieures à celles de la liste B")
    else :
        print("Les températures de la liste B sont en moyennes supérieures à celles de la liste A")

def compareAnnees(lstA, lstB) :
    
    # on s'assure que les deux listes aient la même longueur
    if len(lstA) != len(lstB) :
        print("Erreur : les deux listes n'ont pas la même longueur")
        return None   

    scoreFinal = 0 

    for i in range(len(lstA)) :
        # on récupère les éléments :
        eltA = lstA[i]
        eltB = lstB[i]

        # on effectue la comparaison de eltA et eltB, et 
        # met à jour le scoreFinal en conséquence :
        if eltA > eltB :
            scoreFinal += 1
        else :
            scoreFinal -= 1

    return scoreFinal

question4()
```