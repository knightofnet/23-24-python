#exo debut saisie nom
import tkinter as tk
def viderText(event):
    entree.delete(0,tk.END)

def mafct():
    v2.set(f"Bien le bonjour {v1.get()}")

# etat initial
fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)

lab1 = tk.Label(maFrame, text="Nom ?")
lab1.grid(row=0, column=0, padx=2, pady=2)

v1 = tk.StringVar()
v1.set("Taper votre nom ici")
entree = tk.Entry(maFrame, textvariable=v1, width=30)
entree.grid(row=0, column=1, padx=2, pady=2)
entree.bind("<ButtonRelease>",viderText)

v2 = tk.StringVar()
lab2 = tk.Label(maFrame, textvariable=v2)
lab2.grid(row=1, column=0, columnspan=2, padx=2, pady=5)

b1 = tk.Button(maFrame, text="cliquer", width=8, background="pink", command=mafct)
b1.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

fen.mainloop()