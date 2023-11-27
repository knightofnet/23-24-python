import tkinter as tk

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).pack()
lab1 = tk.Label(mainFrame, text="Choisir un fruit :")
lab1.pack(side=tk.TOP, padx=2, pady=5)

listVal = [ "clémentine", "pomme", "pêche", "kiwi"]
lis1 = tk.Listbox(mainFrame, height=len(listVal))
lis1.pack()
for x in listVal :
    lis1.insert(tk.END, x)
lis1.selection_set(first=2) # pour sélectioner la ligne d'indice 2

root.mainloop()
