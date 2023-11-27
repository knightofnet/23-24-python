import tkinter as tk

# root est le widget racine, celui de la fenêtre
root = tk.Tk()
root.title("Une fenêtre avec Tkinter")

# Un crée un widget Label : une zone qui affiche du texte
w = tk.Label(root, text="Bievenue sous Tkinter :-) ")
w.pack()

# mainloop() lance l'affichage de la root, la fenêtre
root.mainloop()
