import tkinter as tk

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).pack()
lab1 = tk.Label(mainFrame, text="Nom :")
lab1.pack(side=tk.LEFT, padx=2, pady=5)

value = tk.StringVar()
value.set("Texte par défaut")

entree = tk.Entry(mainFrame, textvariable=value, width=30, relief=tk.GROOVE)
entree.pack(padx=2, pady=5)

root.mainloop()
