def affiche(listeChaines1,listeChaines2) :
    if len(listeChaines1) !=len(listeChaines2) :
        print("Pb : nb d’éléments différents")
    else :
        print("Scientifiques :")
        for i in range(0,len(listeChaines1)) :
            s = listeChaines1[i]+" "+listeChaines2[i]
            print(s)
    
# Q2
def construction(lis1, lis2) :
    listRetour = []
    if len(lis1) !=len(lis2) :
        print("Pb : nb d’éléments différents")  
        return listRetour
    
    for i in range(len(lis1)) :
        listRetour.append(lis1[i])
        listRetour.append(lis2[i])
        
    return listRetour
            
lis1=["Albert", "Marie", "Raymond"]
lis2=["Einstein", "Curie", "Poincaré"]
lis3 = construction(lis1,lis2)
print(lis3)
