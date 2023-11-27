import tkinter as tk
import random as random

def afficheIndication(e) :
    a = int(userText.get())
    if (a < tirage) :
        lab2.configure(text="Trop petit")
    elif a > tirage :
        lab2.configure(text="Trop grand")
    else :
        lab2.configure(text="Gagné !")

tirage = random.randint(0,1000)

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).grid()
lab1 = tk.Label(mainFrame, text="Entrez un nombre entre 0 et 1000")
lab1.grid(row=0, column=0)
userText = tk.Entry(mainFrame, width=30, relief=tk.GROOVE)
userText.grid(row=1, column=0)
lab2 = tk.Label(mainFrame )
lab2.grid(row=2, column=0)

userText.bind("<Return>", afficheIndication)

root.mainloop()
