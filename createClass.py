
def createClassStr(nameClass, attr,model) :
    attrList = attr.split(',')

    initParalListStr = ""
    attribsDecl = ""
    for attr in attrList :
        attr = attr.strip(' ')
        paramName = f"p{attr.title()}"
        initParalListStr += f", {paramName}"
        attribsDecl += f"        self.{attr} = {paramName}\n"

    print(model.format(nameClass, initParalListStr, attribsDecl))


classModel = "class {} :\n"
classModel += "    def __init__(self{}) :\n"
classModel += "{}\n"
classModel += "" 
nameClass = "Chien"
attributs = "identification, nom, race, dateNaiss, taille, poids"

createClassStr(nameClass, attributs, classModel)