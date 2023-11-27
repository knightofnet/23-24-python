import tkinter as tk

def handler(e) :
    touche = e.keysym
    if touche == "E" :
        v = tk.Entry(mainFrame, width=30, relief=tk.GROOVE)
        v.pack(padx=2, pady=5)
    if touche == "B" :
        n = tk.Button(mainFrame, width=30, text=entree.get())
        n.pack(padx=2, pady=5)

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).pack()
entree = tk.Entry(mainFrame, width=30, relief=tk.GROOVE, text="Test")
entree.pack(padx=2, pady=5)

# sur le widget entree, en cas d'appuie de touche, appel la fonction handler
entree.bind("<KeyPress>", handler)

root.mainloop()
