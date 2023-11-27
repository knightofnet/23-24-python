"""
Ce code crée une interface graphique simple avec Tkinter, comprenant un cadre avec deux 
labels et un bouton. Les labels affichent du texte avec différentes polices, couleurs de 
fond et de texte. Le bouton, lorsqu'il est cliqué, ferme la fenêtre principale de l'application.
"""

# Importation du module tkinter, souvent abrégé en tk pour simplifier le code
import tkinter as tk

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'. 
# Cet objet représente la fenêtre principale de l'application.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Exemple")

# Création d'un cadre (Frame) dans la fenêtre principale avec un fond de couleur bleu clair.
# Les cadres sont utilisés pour organiser les widgets dans la fenêtre.
frame1 = tk.Frame(root, background="lightblue")
# Positionnement du cadre dans la fenêtre principale.
# - 'padx=20, pady=20' ajoute un espace autour du cadre pour éviter qu'il touche les bords.
# - 'fill=tk.BOTH' indique que le cadre doit s'étendre horizontalement et verticalement pour occuper l'espace alloué.
frame1.pack(padx=20, pady=20, fill=tk.BOTH)

# Création d'un label (Label) dans le cadre frame1.
# - 'text="Hello 1"' définit le texte à afficher dans le label.
# - 'background="purple"' définit la couleur de fond du label.
# - 'font="Arial 24"' définit la police et la taille du texte.
# - 'foreground="white"' définit la couleur du texte.
lab1 = tk.Label(frame1, text="Hello 1", background="purple", font="Arial 24", foreground="white")
# Positionnement du label dans la grille du cadre frame1.
# - 'row=0, column=1' place le label dans la première ligne et la deuxième colonne de la grille.
# - 'padx=10, pady=10' ajoute un espace autour du label.
lab1.grid(row=0, column=1, padx=10, pady=10)

# Création d'un second label dans le cadre frame1 avec des propriétés différentes.
lab2 = tk.Label(frame1, text="Hello2", background="pink", font="Arial 48")
# Positionnement du second label dans la grille du cadre frame1.
# - 'row=1, column=0' place le label dans la deuxième ligne et la première colonne de la grille.
lab2.grid(row=1, column=0, padx=10, pady=10)

# Création d'un bouton (Button) dans le cadre frame1.
# - 'text="fermer"' définit le texte à afficher sur le bouton.
# - 'width=8' définit la largeur du bouton.
# - 'background="darkblue"' et 'foreground="white"' définissent les couleurs du bouton et du texte.
# - 'command=root.destroy' définit l'action à effectuer lorsque le bouton est cliqué (ferme la fenêtre principale).
b1 = tk.Button(frame1, text="fermer", width=8, background="darkblue", foreground="white", command=root.destroy)
# Positionnement du bouton dans la grille du cadre frame1.
# - 'row=2, column=0, columnspan=2' place le bouton dans la troisième ligne, première colonne et il s'étend sur deux colonnes.
b1.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()

