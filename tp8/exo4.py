"""
Roulat : 18.1
Vidal : Défaillant
Tendre : 16.5
"""

def resultat(s) :
    splitted = s.split(" : ")
    return splitted[1].strip("\n")

def repartir(source, admis, ajournes, defaillants) :
    with open(source, "r") as f :
        for ligne in f :
            noteStr = resultat(ligne)
            if noteStr.lower() in ["défaillant", "defaillant"] :
                with open(defaillants, "a") as g :
                    g.write(ligne)
            else :
                note = float(noteStr) 
                if (note < 10 ) :
                    with open(ajournes, "a") as g :
                        g.write(ligne)  
                else :
                     with open(admis, "a") as g :
                        g.write(ligne)                                     


repartir("tp8/notes.txt", "tp8/admis.txt", "tp8/ajournes.txt", "tp8/defaillant.txt")