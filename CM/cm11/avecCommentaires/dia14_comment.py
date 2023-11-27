"""
 Une fenêtre s'ouvre avec un label "Nom :" suivi d'un champ de saisie. 
 Le champ de saisie contient le texte par défaut "Texte par défaut". 
 L'utilisateur peut modifier ce texte.
"""

import tkinter as tk

root = tk.Tk()  # Création de la fenêtre principale
root.title("Une fenêtre avec Tkinter")  # Définition du titre de la fenêtre

mainFrame = tk.Frame(root).pack()  # Création et emballage d'un cadre principal dans la fenêtre

# Création d'un label et son positionnement
lab1 = tk.Label(mainFrame, text="Nom :")  # Création d'un label avec le texte "Nom :"
lab1.pack(side=tk.LEFT, padx=2, pady=5)  # Positionnement du label à gauche avec un peu d'espace autour

# Création d'une variable de contrôle pour un widget Entry
value = tk.StringVar()  # Création d'une instance de StringVar
value.set("Texte par défaut")  # Définition de la valeur par défaut de cette variable

# Création d'un champ de saisie (Entry) et son positionnement
entree = tk.Entry(mainFrame, textvariable=value, width=30, relief=tk.GROOVE)
entree.pack(padx=2, pady=5)  # Positionnement du champ de saisie avec un peu d'espace autour

root.mainloop()  # Lancement de la boucle d'événements
