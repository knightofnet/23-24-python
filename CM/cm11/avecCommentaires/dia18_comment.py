"""
Les boutons radio permettent à l'utilisateur de choisir une seule 
option parmi plusieurs. Dans ce cas, les trois boutons radio 
"Oui", "Non", "Peut-être" sont liés à la même variable (var1). 
Lorsqu'un bouton est sélectionné, var1 prend la valeur associée 
à ce bouton (1, 2 ou 3). 

Seul un bouton radio peut être sélectionné à la fois.
"""

# Importation du module tkinter et renommage en tk pour simplifier son utilisation
import tkinter as tk

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'. 
# Cet objet représente la fenêtre principale de l'application.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Une fenêtre avec Tkinter")

# Création d'un cadre (Frame) dans la fenêtre principale. 
# Les cadres sont utilisés pour organiser les widgets dans la fenêtre.
# La méthode pack() positionne le cadre dans la fenêtre. Sans cet appel, le cadre ne serait pas visible.
mainFrame = tk.Frame(root).pack()

# Création d'une variable de contrôle pour les boutons radio.
# tk.IntVar est une variable spéciale de Tkinter utilisée pour gérer les états des widgets.
var1 = tk.IntVar()

# Création du premier bouton radio (Radiobutton).
# - 'text="Oui"' définit le texte à afficher à côté du bouton radio.
# - 'variable=var1' lie ce bouton radio à la variable var1 créée précédemment.
# - 'value=1' définit la valeur que prendra var1 lorsque ce bouton radio sera sélectionné.
r1 = tk.Radiobutton(mainFrame, text="Oui", variable=var1, value=1)

# Création du deuxième bouton radio de manière similaire au premier, avec un texte et une valeur différents.
r2 = tk.Radiobutton(mainFrame, text="Non", variable=var1, value=2)

# Création du troisième bouton radio de manière similaire aux deux premiers.
r3 = tk.Radiobutton(mainFrame, text="Peut-être", variable=var1, value=3)

# Positionnement des boutons radio dans le cadre.
# - 'anchor=tk.W' positionne chaque bouton radio aligné à gauche (West) dans le cadre.
r1.pack(anchor=tk.W)
r2.pack(anchor=tk.W)
r3.pack(anchor=tk.W)

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()
