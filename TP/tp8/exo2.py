#1
def copier(source, destination):
    f=open(source, 'r')
    g=open(destination, 'w')
    for texte in f:
        g.write(texte)
    f.close()
    g.close()

# 2 
def numeroter(source, destination) :
    with open(source, 'r') as f:    
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                g.write(str(i)+" "+texte)

# 3
def entreCrochet_A(source, destination) :
    f=open(source, 'r')
    g=open(destination, 'w')
    for texte in f:
        g.write("[" + texte[:-1] + "]\n")
    f.close()
    g.close()

def entreCrochet_B(source, destination) :
    with open(source, 'r') as f :
        with open(destination, 'w') as g :
            for texte in f:
                g.write("[" + texte[:-1] + "]\n")
   

entreCrochet_B("tp8\exo1.py", "tp8\exo1_COPY.py")
