def afficherLignesEtLongueur(source):
#On affiche chaque ligne du fichier source et sa longueur.
    try:
        f=open(source, 'r')
        for ligne in f:
            print(ligne)
            lineFeed=0
            if ligne[-1]=='\n':
                lineFeed=1
                print("Longueur :", len(ligne)-lineFeed)
        f.close()
    except IOError:
        print("Lecture du fichier ",source," impossible.")

# Q2
def nombreLignes(source) :
    nbLigne = 0
    try:
        f=open(source, 'r')
        for ligne in f:
            nbLigne += 1
        f.close()

        return nbLigne
    except IOError:
        print("Lecture du fichier ",source," impossible.")

#Q3
def longueurPlusGrandeLigne(source) :
    nMax = 0
    try:
        f=open(source, 'r')
        for ligne in f:
            
            lineFeed=0
            if ligne[-1]=='\n':
                lineFeed=1
                
            lenLigne = len(ligne)-lineFeed

            if lenLigne > nMax :
                nMax = lenLigne
        f.close()

        return nMax
    except IOError:
        print("Lecture du fichier ",source," impossible.")

source="C:\\Users\\arnau\\source\\repos\\23-24-python\\tp8\\alu.txt"
#afficherLignesEtLongueur(source)
print( nombreLignes(source) )
print( longueurPlusGrandeLigne(source) )

#Q4 
f=open("monfichier2.txt", 'w')
f.write(" Hello\ndear")
f.close()

f=open("monfichier2.txt", 'r')
#listLig=f.readlines()
listLig=f.readlines()
f.close()
print(listLig)

