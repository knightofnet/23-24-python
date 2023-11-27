"""
 La Listbox est un widget Tkinter qui affiche une liste d'éléments. 
 Dans ce cas, elle est configurée en mode MULTIPLE, ce qui permet à 
 l'utilisateur de sélectionner plusieurs éléments de la liste en même 
 temps. Les éléments "clémentine", "pomme", "pêche" et "kiwi" sont 
 ajoutés à la liste, et l'utilisateur peut choisir un ou plusieurs fruits.
"""

# Importation du module tkinter, souvent abrégé en tk pour simplifier le code
import tkinter as tk

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'. 
# Cet objet représente la fenêtre principale de l'application.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Une fenêtre avec Tkinter")

# Création d'un cadre (Frame) dans la fenêtre principale et son positionnement avec la méthode grid.
# - 'row=0, column=0' positionne le cadre dans la première ligne et la première colonne de la grille.
# - 'padx=10, pady=10' ajoute un espace autour du cadre pour éviter qu'il touche les bords de la fenêtre.
mainFrame = tk.Frame(root)
mainFrame.grid(row=0, column=0, padx=10, pady=10)

# Création d'un label (Label) et positionnement dans le cadre avec la méthode grid.
# - 'text="Choisir un fruit :"' définit le texte à afficher dans le label.
# - 'row=0, column=0' place le label dans la première ligne et la première colonne de la grille du cadre.
lab1 = tk.Label(mainFrame, text="Choisir un fruit :")
lab1.grid(row=0, column=0)

# Création d'une liste de valeurs à afficher dans la Listbox
listVal = ["clémentine", "pomme", "pêche", "kiwi"]

# Création d'une Listbox (liste) en mode de sélection multiple et son positionnement avec la méthode grid.
# - 'height=len(listVal)' définit la hauteur de la liste pour afficher tous les éléments.
# - 'selectmode=tk.MULTIPLE' permet de sélectionner plusieurs éléments de la liste en même temps.
lis1 = tk.Listbox(mainFrame, height=len(listVal), selectmode=tk.MULTIPLE)
lis1.grid(row=0, column=1, padx=5, pady=5)

# Boucle pour insérer chaque élément de listVal dans la Listbox.
# - 'tk.END' est utilisé pour ajouter chaque nouvel élément à la fin de la liste.
for x in listVal:
    lis1.insert(tk.END, x)

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()
