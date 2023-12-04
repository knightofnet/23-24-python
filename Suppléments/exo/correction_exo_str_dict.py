# exo_str_dict

etudiant = {
    "nom" : "Dupont",
    "prénom" : "Jean",
    "age" : 20,
    "matière préférée" : "Mathématiques"
}

# 2
def afficheDico(dico) :
    for clef in dico :
        print(clef, ":", dico[clef]) 

def afficheDicoBis(dico) :
    for clef, valeur in dico.items() :
        print(clef, ":", valeur) 

afficheDico(etudiant)

# 3
def verifMath(dico) :
    if "Math" in dico["matière préférée"] :
        return True
    return False

def verifMathBis(dico) :
    return "Math" in dico["matière préférée"]

#4 
def countAinName(dico) :
    return dico["nom"].count("a")

#5 
def verif(chaine) :
    if len(chaine) > 30 :
        return False
    
    ensembleChiffre = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "}

    if chaine[0] in ensembleChiffre :
        return False
    
    if chaine[-1] in ensembleChiffre :
        return False
    
    """
    if chaine[0] >= "0" and chaine[0] <= "9" :
        return False
    
    if chaine[-1] >= "0" and chaine[-1] <= "9" :
        return False
    """

    """
    if chaine[-1].isdigit() or chaine[-1] == " " :
        return False
    """

    if chaine.count(" ") > 3 :
        return False

     