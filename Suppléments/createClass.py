# Définition de la fonction createClassStr avec trois paramètres : nameClass, attr et model
def createClassStr(nameClass, attr, model):
    # Séparation des attributs fournis sous forme de chaîne de caractères en une liste d'attributs
    attrList = attr.split(',')

    # Initialisation de deux chaînes vides pour construire les parties du code source
    initParalListStr = ""  # Pour les paramètres du constructeur __init__
    attribsDecl = ""       # Pour l'assignation des attributs dans __init__

    # Itération sur chaque attribut dans la liste d'attributs
    for attr in attrList:
        attr = attr.strip(' ')  # Suppression des espaces inutiles autour de l'attribut
        paramName = f"p{attr.title()}"  # Création du nom du paramètre pour le constructeur

        # Construction de la chaîne de caractères pour les paramètres de __init__
        initParalListStr += f", {paramName}"

        # Construction de la chaîne de caractères pour l'assignation des attributs dans __init__
        attribsDecl += f"        self.{attr} = {paramName}\n"

    # Impression du modèle de classe formaté avec le nom de la classe, les paramètres et l'assignation
    print(model.format(nameClass, initParalListStr, attribsDecl))


# Modèle de classe à utiliser pour la génération du code source de la classe
classModel = "class {} :\n"
classModel += "    def __init__(self{}) :\n"
classModel += "{}\n"
classModel += "" 

# Exemple d'utilisation de la fonction createClassStr
# Définition du nom de la classe et des attributs
nameClass = "Chien"
attributs = "identification, nom, race, dateNaiss, taille, poids"

# Appel de la fonction pour créer et afficher le code source de la classe
createClassStr(nameClass, attributs, classModel)