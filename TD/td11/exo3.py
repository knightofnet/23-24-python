"""
Objectif du jeu et algorithme de vérification :

- Le jeu consiste à prédire la parité (pair ou impair) et la couleur (rouge ou non-rouge) d'un nombre tiré aléatoirement.
- tirageNombre est un entier aléatoire entre 0 et 100, et tirageCouleur est soit 0 soit 1, où 1 représente rouge.
- L'utilisateur fait ses prédictions à l'aide de deux cases à cocher.
- La fonction play vérifie si les prédictions de l'utilisateur correspondent aux résultats du tirage.
- Si les deux prédictions (parité et couleur) sont correctes, l'utilisateur gagne ; sinon, il perd.
- Le résultat est affiché dans l'interface, et le label du résultat change de couleur en rouge si le nombre tiré est rouge.
"""

# Importation des modules nécessaires : 
# - tkinter pour l'interface graphique et 
# - randint pour générer des nombres aléatoires
import tkinter as tk
from random import randint

# Définition de la fonction play, qui est appelée lorsque l'utilisateur clique sur le bouton "jouer"
def play():
    # Récupération du choix de l'utilisateur concernant la parité du nombre (pair ou impair)
    # Si la case liée à vChiffre est cochée, donc que vChiffre.get() == 1, alors c'est que le joueur prédit
    # que le nombre est pair.
    joueurEstPair = vChiffre.get() == 1

    # Récupération du choix de l'utilisateur concernant la couleur (rouge ou non)
    # Si la case liée à vCouleur est cochée, donc que vCouleur.get() == 1, alors c'est que le joueur prédit
    # que la couleure est rouge.
    joueurEstRouge = vCouleur.get() == 1

    # Initialisation de la variable estGagne à False. 
    # Elle sera utilisée pour déterminer si le joueur a gagné.
    estGagne = False

    # Vérification si le nombre tiré correspond au choix de parité de l'utilisateur
    if (tirageNombre % 2 == 0 and joueurEstPair) or (tirageNombre % 2 != 0 and not joueurEstPair):
        estGagne = True
    
    # Vérification si la couleur tirée correspond au choix de couleur de l'utilisateur
    if (tirageCouleur == 1 and joueurEstRouge) or (tirageNombre == 0 and not joueurEstRouge):
        # Si le joueur a déjà réussi la première vérification, il continue d'être en lice pour gagner
        estGagne = estGagne and True
    else:
        # Si la couleur ne correspond pas, le joueur perd indépendamment de la parité
        estGagne = False
        # On aurait pu écrire ici : estGagne = estGagne and False, mais ça résultera
        # toujours False, donc autant mettre directement False.

    # Mise à jour du label avec le résultat du jeu
    if estGagne:
        # Si estGagne est True, le joueur a gagné
        vResult.set("Gagné !")
    else:
        # Sinon, le joueur a perdu et le nombre tiré est affiché
        vResult.set(f"{tirageNombre} perdu !")
        if tirageCouleur == 1:
            # Si la couleur tirée est rouge, change la couleur du texte du label en rouge
            lab3.configure(foreground="red")


# Génération des nombres aléatoires pour le tirage (parité et couleur)
tirageNombre = randint(0, 100)
tirageCouleur = randint(0, 1)

# Affichage du tirage dans la console pour le débogage
print(tirageNombre, tirageCouleur)

# Configuration de la fenêtre principale
fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)

# Création et positionnement des widgets dans la fenêtre
lab1 = tk.Label(maFrame, text="Un chiffre noir ou rouge va sortir...\nCliquez ce que vous pensez obtenir :")
lab1.grid(row=0, column=0, columnspan=2, padx=2, pady=2)

# Configuration des boutons de choix pour la parité et la couleur
vChiffre = tk.IntVar()
r1 = tk.Checkbutton(maFrame, text="chiffre pair", variable=vChiffre)
r1.grid(row=1, column=0, padx=10, pady=10)

vCouleur = tk.IntVar()
r2 = tk.Checkbutton(maFrame, text="rouge", variable=vCouleur)
r2.grid(row=1, column=1, padx=10, pady=10)

# Label pour afficher le résultat du jeu
vResult = tk.StringVar()
lab3 = tk.Label(maFrame, text="", background="lightblue", textvariable=vResult)
lab3.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

# Bouton pour lancer le jeu
button = tk.Button(maFrame, text="jouer", background="green", command=play)
button.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

# Lancement de la boucle principale de Tkinter
fen.mainloop()
