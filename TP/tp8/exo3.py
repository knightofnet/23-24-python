# 1
def ecrire(nom, n) :
    with open(nom, "w") as f :
        for i in range(1, n + 1) :
            f.write(f"Texte de la ligne n°{i}\n")

def ecrireAlternative(nom, n) :
    f = open(nom, "w")
    for i in range(1, n + 1) :
        f.write(f"Texte de la ligne n°{i}\n")
    f.close()

ecrire("tp8/ficE3q1.txt", 3)

# 2
def copierFin(source, destination,n) :
    """Cette fonction copie le fichier source, dans le fichier de destination, en commençant à la ligne n"""
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i>=n:
                    g.write(texte)

copierFin("tp8/exo1.py", "tp8/exo1_E3Q2.py", 3)
# Cette fonction copie le fichier source, dans le
# fichier de destination, en commençant à la ligne n

def copierEntre(source, destination, n, m) :
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if n <= i <= m:
                    g.write(texte)

copierEntre("tp8/exo1.py", "tp8/exo1_E3Q3.py", 3, 5)

def copierLignesPaires(source, destination):
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i % 2 == 0 :
                    g.write(texte)

copierLignesPaires("tp8/exo1.py", "tp8/exo1_E3Q4_paires.py")

def copierLignesImpaires(source,destination) :
    with open(source, 'r') as f:
        with open(destination, 'w') as g:
            i=0
            for texte in f:
                i+=1
                if i % 2 != 0 :
                    g.write(texte)

copierLignesImpaires("tp8/exo1.py", "tp8/exo1_E3Q4_impaires.py")