import tkinter as tk

root = tk.Tk()
root.title("Une fenêtre avec Tkinter")

frame1 = tk.Frame(root, borderwidth=2, background="green")
frame1.pack(pady=10, padx=10, fill=tk.BOTH)

frame2 = tk.Frame(frame1, borderwidth=3, background="red", relief=tk.GROOVE)
frame2.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(frame1, text="Texte dans la frame1").pack(side=tk.TOP)
tk.Label(frame2, text="Texte dans la frame2").pack()

root.mainloop()
