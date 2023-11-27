"""
Ce code crée une fenêtre avec un seul widget (Label) qui affiche 
un texte. La méthode mainloop() est essentielle car elle permet 
à la fenêtre de rester ouverte et de réagir aux actions de l'utilisateur.
"""

# Importation du module tkinter et renommage en tk pour simplifier son utilisation
import tkinter as tk

# Création de la fenêtre principale ('root') de l'application Tkinter
root = tk.Tk()

# Définition du titre de la fenêtre principale
root.title("Une fenêtre avec Tkinter")

# Création d'un widget 'Label' (étiquette). 
# Un widget est un élément d'interface graphique, ici un 'Label' pour afficher du texte.
# - Le premier paramètre 'root' indique que ce Label sera placé dans la fenêtre principale.
# - 'text' est une propriété qui définit le texte à afficher dans le Label.
w = tk.Label(root, text="Bienvenue sous Tkinter :-) ")

# La méthode 'pack' est utilisée pour ajouter le widget à la fenêtre principale ('root').
# Elle positionne le widget dans la fenêtre. Sans cet appel, le widget ne serait pas visible.
w.pack()

# La méthode 'mainloop' est appelée sur l'objet 'root'. 
# Cette méthode lance la boucle principale de l'application.
# Elle attend que des événements se produisent dans l'interface (comme des clics de souris ou des entrées clavier)
# et les traite jusqu'à ce que la fenêtre soit fermée.
root.mainloop()
