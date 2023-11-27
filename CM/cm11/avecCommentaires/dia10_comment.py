"""
Ce code crée une interface graphique simple avec une fenêtre contenant 
un cadre et un bouton. Lorsque l'utilisateur clique sur le bouton, 
le message "Hello world !" est affiché dans la console. C'est un 
exemple basique de la façon dont les éléments de l'interface graphique 
sont créés et organisés en Tkinter, et comment les interactions 
utilisateur (comme les clics de bouton) sont gérées.
"""

# Importation du module tkinter, souvent abrégé en tk pour simplifier le code
import tkinter as tk

# Définition d'une fonction qui sera appelée lorsque le bouton est cliqué
def ecrire_console():
    print("Hello world !")  # Affiche le message "Hello world !" dans la console

# Création de l'objet principal de l'application Tkinter, souvent appelé 'root'. 
# Cet objet représente la fenêtre principale de l'application.
root = tk.Tk()

# Définition du titre de la fenêtre principale.
root.title("Une fenêtre avec Tkinter")

# Création d'un cadre (Frame) dans la fenêtre principale. 
# Les cadres sont utilisés pour organiser les widgets dans la fenêtre.
mainFrame = tk.Frame(root).pack()  # La méthode pack() positionne le cadre dans la fenêtre.

# Création d'un bouton (Button) et placement dans le cadre principal.
# - 'text' définit le texte à afficher sur le bouton.
# - 'command' définit la fonction à appeler lorsque le bouton est cliqué (ici ecrire_console).
button = tk.Button(mainFrame, text="Cliquez sur ce bouton", command=ecrire_console)

# Positionnement du bouton dans le cadre.
# - 'side=tk.LEFT' positionne le bouton sur le côté gauche du cadre.
# - 'padx' et 'pady' ajoutent un espace autour du bouton pour éviter qu'il touche les bords.
button.pack(side=tk.LEFT, padx=10, pady=10)

# Lancement de la boucle principale de Tkinter.
# Cette boucle maintient la fenêtre ouverte et attend les actions de l'utilisateur.
root.mainloop()
