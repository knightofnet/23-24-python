import tkinter as tk
root = tk.Tk()
root.title("Exemple")

frame1 = tk.Frame(root, background="lightblue")
frame1.pack(padx=20, pady=20, fill=tk.BOTH)

lab1 = tk.Label(frame1, text="Hello 1",background="purple",font="Arial 24",foreground="white")
lab1.grid(row=0, column=1, padx=10, pady=10)

lab2 = tk.Label(frame1, text="Hello2", background="pink", font="Arial 48")
lab2.grid(row=1, column=0, padx=10, pady=10)

b1 = tk.Button(frame1, text="fermer", width=8, background="darkblue",
foreground="white",command=root.destroy)
b1.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

root.mainloop()