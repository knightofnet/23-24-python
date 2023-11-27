import tkinter as tk

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).pack()

var1 = tk.IntVar()
r1 = tk.Radiobutton(mainFrame, text="Oui", variable=var1, value=1)
r2 = tk.Radiobutton(mainFrame, text="Non", variable=var1, value=2)
r3 = tk.Radiobutton(mainFrame, text="Peut-être", variable=var1, value=3)
r1.pack(anchor=tk.W)
r2.pack(anchor=tk.W)
r3.pack(anchor=tk.W)

root.mainloop()
