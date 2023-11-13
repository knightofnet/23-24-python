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
  
# Q3 
def eclatement(lis) :
    retLis1 = []
    retLis2 = []
    
    for i in range(len(lis)) :
        listDestination = retLis2
        if i % 2 == 0 :
            listDestination = retLis1
        listDestination.append(lis[i])
            
    return (retLis1, retLis2)

# Réponse alternative en utilisant le slicing sur lis
def eclatement_slicing(lis) :           
    return (lis[::2], lis[1::2] )
  
# Q4
def rassemble(lis) :
    listRetour = []
   
    if len(lis) % 2 != 0:
        return listRetour

    
    for i in range(0, len(lis), 2) :
        s = lis[i] + " " + lis[i + 1]
        print(s)
        listRetour.append(s)
        
    return listRetour
        
        
lis1=["Albert", "Marie", "Raymond"]
lis2=["Einstein", "Curie", "Poincaré"]
lis3 = construction(lis1,lis2)

nouvelleLis1, nouvelleLis2 = eclatement(lis3)
print("nv1:", nouvelleLis1, "nv2", nouvelleLis2)

print( rassemble(lis3) )
