listeTuple  = [ ("janvier", 1), ("février", 2), ("mars", 3) ]

dico = {}
for tuple in listeTuple :
    clef = tuple[0]
    valeur = tuple[1]
    dico[clef] = valeur

for clef, valeur in listeTuple :
    dico[clef] = valeur

print(dico)


lstClef = sorted(dico.keys())
for clef in lstClef :
    print(clef, ":", dico[clef])

raise ValueError("J'ai envi que ça plante")