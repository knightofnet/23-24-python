import tkinter as tk

# création de la fenêtre et et de frame
root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root)
mainFrame.grid(row=0, column=0, padx=10, pady=10)

# création de label
lab1 = tk.Label(mainFrame, text="Choisir un fruit :")
lab1.grid(row=0, column=0)

# création de la listbox     
listVal = [ "clémentine", "pomme", "pêche", "kiwi"]
lis1 = tk.Listbox(mainFrame, height=len(listVal), selectmode=tk.MULTIPLE)
lis1.grid(row=0, column=1, padx=5, pady=5)
for x in listVal :
    lis1.insert(tk.END, x)

root.mainloop()
