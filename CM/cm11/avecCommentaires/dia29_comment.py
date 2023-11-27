"""
Explication du concept de liaison d'événements : Dans ce code, un champ 
de saisie est créé, et un gestionnaire d'événements (handler) est associé
à cet élément pour réagir aux pressions de touches. Si l'utilisateur presse 
la touche "E", un nouveau champ de saisie est créé. Si la touche "B" est 
pressée, un bouton portant le texte actuel du champ de saisie est créé. 

Cela démontre comment Tkinter peut être utilisé pour créer des interfaces 
interactives qui réagissent aux actions de l'utilisateur.
"""

# Importation du module tkinter, souvent abrégé en tk pour simplifier le code
import tkinter as tk

# Définition d'une fonction qui sera appelée lorsqu'une touche est pressée dans le champ de saisie
def handler(e):
    touche = e.keysym  # Récupération de la touche pressée
    if touche == "E":  # Si la touche pressée est "E"
        # Création d'un nouveau champ de saisie (Entry) et positionnement dans le cadre
        v = tk.Entry(mainFrame, width=30, relief=tk.GROOVE)
        v.pack(padx=2, pady=5)
    if touche == "B":  # Si la touche pressée est "B"
        # Création d'un nouveau bouton (Button) avec le texte récupéré du champ de saisie
        # et positionnement dans le cadre
        n = tk.Button(mainFrame, width=30, text=entree.get())
        n.pack(padx=2, pady=5)

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Une fenêtre avec Tkinter")

# Création d'un cadre (Frame) dans la fenêtre principale et son positionnement.
mainFrame = tk.Frame(root).pack()

# Création d'un champ de saisie (Entry) et positionnement dans le cadre.
entree = tk.Entry(mainFrame, width=30, relief=tk.GROOVE, text="Test")
entree.pack(padx=2, pady=5)

# Liaison d'un événement de pression de touche au champ de saisie.
# En cas d'appui sur une touche, la fonction 'handler' est appelée.
entree.bind("<KeyPress>", handler)

# Lancement de la boucle principale de Tkinter.
root.mainloop()
