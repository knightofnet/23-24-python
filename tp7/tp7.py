def exo2() :

    print(fnC(27, 6))
    assert fnC(27, 6) == 296010

def fnC(n, p) :
    # cas de base
    if p == 0 or p == n :
        return 1
    # cas récursif
    return fnC(n - 1, p-1) + fnC(n - 1, p)

def exo3() :
    l1 = [1, -2, 6, -4, 7, -12, -2, 5]
    l2 = [-2, 8, -9 , 20, -14, 6, -3, -3]

    l3 = listeSansDoublons(l1)
    print(l3)

    l4 = valeursCommunes(l1, l2)
    print(l4)

def listeSansDoublons(lst) :
    setL = set(lst)
    return sorted( list(setL) )

def valeursCommunes(lst1, lst2) :
    e1 = set(lst1)
    e2 = set(lst2)

    e3 = e2 & e1
    l = list(e3) 

    return l

def valeursCommunesBis(lst1, lst2) :
    return list(set(lst1) & set(lst2)) 

def exo4() :
    maliste = list("Un Texte")
    print(maliste)
    monEnsemble = set("Un Texte")
    print(monEnsemble)

    assert memesLettres("abccd", "cabdda")
    assert memesLettres("abccd", "fgtt") == False

def memesLettres(s1, s2) :
    e1 = set(s1)
    e2 = set(s2)
    print( e1 == e2 )
    return e1 == e2 

def memesLettresBis(s1, s2) :
    return set(s1) == set(s2)

def exo5() :
    dico = {25:4, 8:1, 12:2 , 3:5 }
    print(dico)
    print("5 dans dico ? ", (5 in dico) )
    print("25 dans dico ? ", (25 in dico) )
    dico[9]=1
    dico[8]=2
    print(dico)
    del dico[25]
    print(dico)

def exo5_suite_et_6() :
    inventaire = {'orange':378, 'pomme':545, 'banane':422, 'poire' : 269 }   

    #afficheEstPresent(inventaire)

    #modifieFruit(inventaire)
    print(inventaire)
    supprimeFruit(inventaire)
    print(inventaire)

    print(nombre(inventaire))
    print(stockTotal(inventaire))
    afficheStock(inventaire)
    
def afficheEstPresent(inventaire) :
    choiceFruit =  input("Choisissez un fruit :")
    choiceFruit = choiceFruit.lower()

    if choiceFruit in inventaire :
        print("Stock de", choiceFruit, "est", inventaire[choiceFruit])
    else :
        print("Le fruit n'est pas en stock")

def modifieFruit(d) :
    choiceFruit =  input("Choisissez un fruit :")
    choiceFruit = choiceFruit.lower()

    nvStock = int(input("Quel stock ?"))

    if choiceFruit in d :
        d[choiceFruit] += nvStock
    else :
        d[choiceFruit] = nvStock

def supprimeFruit(d) : 
    choiceFruit =  input("Choisissez un fruit :")
    choiceFruit = choiceFruit.lower()

    if choiceFruit in d :
        del d[choiceFruit]
    else :
        print("Le fruit n'est pas en stock")

def nombre(d) :
    cpt = 0
    for elt in d :
        cpt += 1    
    return cpt

def nombreBis(d) :
    return len(d)

def stockTotal(d) :
    cpt = 0
    for elt in d.values() :
        cpt += elt    
    return cpt

def stockTotalBis(d) :
    return sum(list(d.values()))

def afficheStock(d) :
    e = sorted(d.keys())
    for k in e :
          print("fruit :", k, ", stock :", d[k])
    

exo5_suite_et_6()