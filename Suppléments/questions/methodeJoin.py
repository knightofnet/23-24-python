lst = [13, 55, 100]

# dans le cas de liste composées d'élément de type autre que les chaines de caractères, il est nécessaire d'effectuer une transformation avant d'utiliser la méthode join().

# Version 1 :
nouvelleListe = []
for elt in lst :
    nouvelleListe.append(str(elt))

listeJointe = "#".join(nouvelleListe)

# Version 2 (avec compréhension de liste) :
listeJointe = "#".join([ str(elt) for elt in lst ])

print(listeJointe)