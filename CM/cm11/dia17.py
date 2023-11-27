import tkinter as tk
root = tk.Tk()
root.title("Une fenêtre avec Tkinter")
mainFrame = tk.Frame(root).pack()

var1 = tk.IntVar()
c1 = tk. Checkbutton (mainFrame, text = "Case 1", variable = var1)
c1.pack()

var2 = tk.IntVar()
c2 = tk. Checkbutton (mainFrame, text = "Case 2", variable = var2, state=tk.DISABLED)
c2.pack()

root.mainloop()
