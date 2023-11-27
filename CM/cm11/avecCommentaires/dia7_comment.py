"""
Ce code est un exemple plus complexe, utilisant des cadres (frames) 
imbriqués et des labels pour organiser le contenu de l'interface
graphique. Les 'Frames' servent à structurer l'interface en sections, 
tandis que les 'Labels' affichent des textes dans ces sections.
"""

# Importation du module tkinter, souvent abrégé en tk pour simplifier le code
import tkinter as tk

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'. 
# Cet objet représente la fenêtre principale de l'application.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Une fenêtre avec Tkinter")

# Création d'un 'Frame' dans la fenêtre principale.
# Un 'Frame' est un conteneur qui peut contenir d'autres widgets.
# - 'borderwidth' définit l'épaisseur de la bordure du cadre.
# - 'background' définit la couleur de fond du cadre.
frame1 = tk.Frame(root, borderwidth=2, background="green")

# Ajout du 'Frame' à la fenêtre principale ('root') avec quelques configurations supplémentaires.
# - 'pady' et 'padx' ajoutent un espace vertical et horizontal autour du cadre.
# - 'fill=tk.BOTH' indique que le cadre doit s'étendre dans les deux directions (verticale et horizontale) pour occuper l'espace alloué.
frame1.pack(pady=10, padx=10, fill=tk.BOTH)

# Création d'un second 'Frame' dans le premier cadre ('frame1').
# Cette fois, on utilise le style 'relief=tk.GROOVE' pour donner un aspect en relief au cadre.
frame2 = tk.Frame(frame1, borderwidth=3, background="red", relief=tk.GROOVE)

# Ajout du second 'Frame' à 'frame1' avec configuration de son positionnement.
# - 'side=tk.RIGHT' positionne ce cadre à droite dans son conteneur.
# - 'padx' et 'pady' ajoutent un espace autour du cadre pour éviter qu'il touche les bords.
frame2.pack(side=tk.RIGHT, padx=10, pady=10)

# Création d'un widget 'Label' (étiquette) dans 'frame1'.
# Le texte "Texte dans la frame1" s'affiche dans ce label.
# 'side=tk.TOP' positionne le label en haut dans le cadre 'frame1'.
tk.Label(frame1, text="Texte dans la frame1").pack(side=tk.TOP)

# Création d'un autre widget 'Label' dans 'frame2'.
# Le texte "Texte dans la frame2" s'affiche dans ce second label.
# Sans spécification, le label s'ajoute par défaut en haut du cadre 'frame2'.
tk.Label(frame2, text="Texte dans la frame2").pack()

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()
