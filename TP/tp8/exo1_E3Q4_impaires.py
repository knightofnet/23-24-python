def afficherLignesEtLongueur(source):
    try:
        for ligne in f:
            lineFeed=0
                lineFeed=1
        f.close()
        print("Lecture du fichier ",source," impossible.")
# Q2
    nbLigne = 0
        f=open(source, 'r')
            nbLigne += 1

    except IOError:

def longueurPlusGrandeLigne(source) :
    try:
        for ligne in f:
            lineFeed=0
                lineFeed=1
            lenLigne = len(ligne)-lineFeed
            if lenLigne > nMax :
        f.close()
        return nMax
        print("Lecture du fichier ",source," impossible.")
source="C:\\Users\\arnau\\source\\repos\\23-24-python\\tp8\\alu.txt"
print( nombreLignes(source) )

f=open("monfichier2.txt", 'w')
f.close()
f=open("monfichier2.txt", 'r')
listLig=f.readlines()
print(listLig)
