import tkinter as tk
def ecrire_console() :
    print("Hello world !")

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")

mainFrame = tk.Frame(root).pack()
button = tk.Button(mainFrame, text="Cliquez sur ce bouton", command=ecrire_console)
button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
