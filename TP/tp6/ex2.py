for i in range(32,128):
    print(i,":",chr(i)," ; ",end='')
    print()
    
    
def parcourir(s) :
    longueur = len(s)
    print("Longueur :", longueur)
    for i in range(longueur) :
        print("Caractère n° {} : {} code ASCII : {}".format(i, s[i], ord(s[i])))

parcourir("Texte")

def grec() :
    minuscules = ""
    for i in range(945, 969 + 1) :
        minuscules += chr(i)
        
    maj = ""
    for i in range(913, 937 + 1) :
        maj += chr(i)
        
    return (minuscules, maj)

print(grec())