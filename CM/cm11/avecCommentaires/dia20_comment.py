"""
La Listbox est un widget Tkinter qui affiche une liste d'éléments 
parmi lesquels l'utilisateur peut choisir. Dans cet exemple, la 
Listbox est utilisée pour afficher une liste de fruits, et l'élément 
"pêche" est sélectionné par défaut. L'utilisateur peut sélectionner 
un autre fruit dans la liste si souhaité.
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

# Création d'un label (Label) et positionnement dans le cadre.
# - 'text="Choisir un fruit :"' définit le texte à afficher dans le label.
# - 'side=tk.TOP' positionne le label en haut (TOP) du cadre.
lab1 = tk.Label(mainFrame, text="Choisir un fruit :")
lab1.pack(side=tk.TOP, padx=2, pady=5)

# Création d'une liste de valeurs à afficher dans la Listbox
listVal = ["clémentine", "pomme", "pêche", "kiwi"]

# Création d'une Listbox (liste) et positionnement dans le cadre.
# - 'height=len(listVal)' définit la hauteur de la liste pour afficher tous les éléments.
lis1 = tk.Listbox(mainFrame, height=len(listVal))
lis1.pack()

# Boucle pour insérer chaque élément de listVal dans la Listbox.
# - 'tk.END' est utilisé pour ajouter chaque nouvel élément à la fin de la liste.
for x in listVal:
    lis1.insert(tk.END, x)

# Sélection par défaut de l'élément à l'indice 2 dans la liste (dans ce cas, "pêche").
lis1.selection_set(first=2)

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()
