import tkinter as tk
from random import randint

def play() :
    joueurEstPair = vChiffre.get() == 1
    joueurEstRouge = vCouleur.get() == 1

    estGagne = False

    if (tirageNombre%2 == 0 and joueurEstPair) or (tirageNombre%2 != 0 and joueurEstPair == False) :
        estGagne = True
    
    if (tirageCouleur == 1 and joueurEstRouge) or (tirageNombre == 0 and joueurEstRouge == False) :
        estGagne = estGagne and True
    else :
        estGagne = False

    if estGagne :
        vResult.set("Gagné !")
    else :
        vResult.set(f"{tirageNombre} perdu !")
        if tirageCouleur == 1 :
            lab3.configure(foreground="red")
            

tirageNombre = randint(0, 100)
tirageCouleur = randint(0,1)

print(tirageNombre, tirageCouleur)
fen = tk.Tk()
maFrame = tk.Frame(fen)
maFrame.pack(padx=20, pady=10)

lab1 = tk.Label(maFrame, text="Un chiffre noir ou rouge va sortir...\nCliquez ce que vous pensez obtenir :")
lab1.grid(row=0, column=0, columnspan=2, padx=2, pady=2)

vChiffre = tk.IntVar()
r1 = tk.Checkbutton(maFrame, text="chiffre pair", variable=vChiffre)
r1.grid(row=1, column=0, padx=10, pady=10)

vCouleur = tk.IntVar()
r2 = tk.Checkbutton(maFrame, text="rouge", variable=vCouleur)
r2.grid(row=1, column=1, padx=10, pady=10)

vResult = tk.StringVar()
lab3 = tk.Label(maFrame, text="", background="lightblue", textvariable=vResult)
lab3.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

button = tk.Button(maFrame, text="jouer", background="green", command=play)
button.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

fen.mainloop()