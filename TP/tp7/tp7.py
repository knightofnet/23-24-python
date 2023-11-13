# Exercice 2 - Récurtion et Coefficients Binomiaux
# ------------

def exo2() :
    print(fnC(27, 6))
    assert fnC(27, 6) == 296010

def fnC(n, p) :
    # La fonction calcule le coefficient binomial de n parmi p
    # Cas de base : si p est 0 ou égal à n, le résultat est 1
    if p == 0 or p == n :
        return 1
    # Appel récursif : on réduit progressivement les valeurs de n et p
    return fnC(n - 1, p-1) + fnC(n - 1, p)

#exo2()


# Exercice 3 - Manipulation de Listes et Ensembles
# ------------

def exo3() :
    # Initialisation des listes de nombres
    l1 = [1, -2, 6, -4, 7, -12, -2, 5]
    l2 = [-2, 8, -9 , 20, -14, 6, -3, -3]

    # Elimination des doublons dans l1 et affichage
    l3 = listeSansDoublons(l1)
    print(l3)

    # Trouver les éléments communs entre l1 et l2 et les afficher
    l4 = valeursCommunes(l1, l2)
    print(l4)

# Crée un ensemble à partir de la liste pour éliminer les doublons, puis trie et renvoie le résultat
def listeSansDoublons(lst) :
    setL = set(lst)
    return sorted(list(setL))

# Utilise l'intersection d'ensembles pour trouver les valeurs communes
def valeursCommunes(lst1, lst2) :
    e1 = set(lst1)
    e2 = set(lst2)
    e3 = e2 & e1
    l = list(e3) 
    return l

#exo3()


# Exercice 4 - Comparaison d'Ensembles
# ------------

def exo4() :
    # Conversion d'une chaîne en liste et en ensemble pour démonstration
    maliste = list("Un Texte")
    print(maliste)
    monEnsemble = set("Un Texte")
    print(monEnsemble)

    # Vérification si deux chaînes contiennent les mêmes lettres
    assert memesLettres("abccd", "cabdda")
    assert memesLettres("abccd", "fgtt") == False

# Compare les ensembles de caractères des deux chaînes
def memesLettres(s1, s2) :
    e1 = set(s1)
    e2 = set(s2)
    print(e1 == e2)
    return e1 == e2

#exo4()


# Exercice 5 - Manipulation de Dictionnaires
# ------------

def exo5() :
    # Initialisation d'un dictionnaire avec des clés et valeurs
    dico = {25:4, 8:1, 12:2 , 3:5 }
    print(dico)
    print("5 dans dico ? ", (5 in dico))
    print("25 dans dico ? ", (25 in dico))
    dico[9]=1
    dico[8]=2
    print(dico)
    del dico[25]
    print(dico)


# Exercice 5/6 - Fonctions Avancées sur les Dictionnaires
# ------------

def exo5_suite_et_6() :
    # Initialisation d'un inventaire de fruits
    inventaire = {'orange':378, 'pomme':545, 'banane':422, 'poire' : 269 }

    print(inventaire)
    supprimeFruit(inventaire)
    print(inventaire)

    # Affiche le nombre de fruits dans l'inventaire et le stock total
    print(nombre(inventaire))
    print(stockTotal(inventaire))
    afficheStock(inventaire)

def afficheEstPresent(inventaire) :
    # Demande à l'utilisateur de saisir le nom d'un fruit
    choiceFruit =  input("Choisissez un fruit :")
    # Convertit le nom du fruit en minuscules pour une comparaison cohérente
    choiceFruit = choiceFruit.lower()

    # Vérifie si le fruit est présent dans l'inventaire
    if choiceFruit in inventaire :
        print("Stock de", choiceFruit, "est", inventaire[choiceFruit])
    else :
        print("Le fruit n'est pas en stock")

def modifieFruit(d) :
    # Demande le nom du fruit à modifier
    choiceFruit =  input("Choisissez un fruit :")
    choiceFruit = choiceFruit.lower()

    # Demande la quantité de stock à ajouter (ou soustraire)
    nvStock = int(input("Quel stock ?"))

    # Met à jour le stock du fruit dans le dictionnaire
    if choiceFruit in d :
        d[choiceFruit] += nvStock
    else :
        # Si le fruit n'est pas dans l'inventaire, l'ajoute avec le nouveau stock
        d[choiceFruit] = nvStock

def supprimeFruit(d) : 
    # Demande le nom du fruit à supprimer
    choiceFruit =  input("Choisissez un fruit :")
    choiceFruit = choiceFruit.lower()

    # Supprime le fruit de l'inventaire s'il existe
    if choiceFruit in d :
        del d[choiceFruit]
    else :
        print("Le fruit n'est pas en stock")

def nombre(d) :
    # Compte le nombre de fruits dans l'inventaire
    cpt = 0
    for elt in d :
        cpt += 1    
    return cpt

# Version plus simple utilisant len pour obtenir la taille du dictionnaire
def nombreBis(d) :
    return len(d)

def stockTotal(d) :
    # Calcule la quantité totale de tous les fruits dans l'inventaire
    cpt = 0
    for elt in d.values() :
        cpt += elt    
    return cpt

# Utilise sum pour calculer le total en une seule ligne
def stockTotalBis(d) :
    return sum(d.values())

def afficheStock(d) :
    # Trie les fruits par ordre alphabétique de leurs noms
    e = sorted(d.keys())
    # Affiche le stock de chaque fruit
    for k in e :
        print("fruit :", k, ", stock :", d[k])


# Chaque fonction illustre une manipulation spécifique des dictionnaires en Python, 
# en mettant en œuvre des concepts tels que la saisie utilisateur, la mise à jour, 
# la suppression d'éléments, et l'itération à travers des collections.

exo5()
exo5_suite_et_6()