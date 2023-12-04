import tkinter as tk
from random import randint

class Essai1(object):
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.lab1 = tk.Label(self.frame, text="Choisissez :")
        self.lab1.grid(row=0, column=0)

        self.frame2 = tk.Frame(self.frame, background="lightblue")
        self.frame2.grid(row=0, column=1)

        self.btn = tk.Button(self.frame, text="alors?", background="green", command=self.mafct)
        self.btn.grid(row=1, column=0, columnspan=2)

        self.var2 = tk.StringVar()
        self.lab2 = tk.Label(self.frame, textvariable=self.var2, background="orange")
        self.lab2.grid(row=2, column=0, columnspan=2)

        self.listGateaux = ["Saint-Honoré", "Opéra", "Mille-feuilles", "Religieuse au café", "TiraMisu"]

        self.var1 = tk.IntVar()

        self.listbox = tk.Listbox(self.frame2, height=len(self.listGateaux))
        self.listbox.pack()
        for elt in self.listGateaux :
            self.listbox.insert(tk.END, elt) 
            

    def mafct(self):
        tirage = randint(0, len(self.listGateaux) - 1)
        tirageGateau = self.listGateaux[tirage]
        eltSelected = self.listbox.curselection()

        if len(eltSelected) > 0 and tirage == eltSelected[0] :
            self.var2.set(f"Excellent choix, l'ordi adore {tirageGateau}")
        else :
            self.var2.set(f"Tsss pas bon, l'ordi préfère {tirageGateau}")


def main():
    root = tk.Tk()
    app = Essai1(root)
    root.mainloop()

if __name__ == '__main__':
    main()