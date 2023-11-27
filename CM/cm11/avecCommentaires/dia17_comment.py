"""
Une fenêtre s'ouvre avec deux cases à cocher. 
La première, "Case 1", est activable et désactivable 
par l'utilisateur. La seconde, "Case 2", est 
désactivée (grisée) et ne peut pas être modifiée par l'utilisateur
"""

import tkinter as tk

root = tk.Tk()  # Création de la fenêtre principale
root.title("Une fenêtre avec Tkinter")  # Définition du titre de la fenêtre

mainFrame = tk.Frame(root).pack()  # Création et emballage d'un cadre principal dans la fenêtre

# Création de la première case à cocher
var1 = tk.IntVar()  # Variable de contrôle pour la case à cocher
c1 = tk.Checkbutton(mainFrame, text="Case 1", variable=var1)  # Création de la case à cocher
c1.pack()  # Positionnement de la case à cocher

# Création de la seconde case à cocher, désactivée
var2 = tk.IntVar()  # Variable de contrôle pour la seconde case à cocher
c2 = tk.Checkbutton(mainFrame, text="Case 2", variable=var2, state=tk.DISABLED)  # Case à cocher désactivée
c2.pack()  # Positionnement de la seconde case à cocher

root.mainloop()  # Lancement de la boucle d'événements
