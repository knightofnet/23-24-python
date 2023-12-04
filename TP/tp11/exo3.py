# jeu du 421
import tkinter as tk

def dessineDe(n,taille,x,y):
    """ n nb de faces, taille 8 convient"""   
    #carre externe
    canvas.create_rectangle(x,y, x+(10*taille),
                                y+(10*taille), fill='white')
    if n>=1 and n<=6:
        #liste des coord. des cercles pour chaque face
        coords = [[(4,4)],
                  [(1,1),(7,7)],
                  [(1,7),(4,4),(7,1)],
                  [(1,1),(7,1),(1,7),(7,7)],
                  [(1,1),(7,1),(1,7),(7,7),(4,4)],
                  [(2,1),(6,1),(2,4),(6,4),(2,7),(6,7)]]
        
        for p in coords[n-1]:
                canvas.create_oval(x+(p[0]*taille),
                                   y+(p[1]*taille),
                                   x+((p[0]+2)*taille),
                                   y+((p[1]+2)*taille), fill='black')
            

fenetre = tk.Tk()
fenetre.title("Jeu du 421")
fr = tk.Frame(fenetre)
fr.pack(padx=20, pady=10)

canvas = tk.Canvas(fr, width=440, height=120, bg="lightpink")
de1=6
dessineDe(de1,8,20,20)
de2=6
dessineDe(de2,8,180,20)
de3=6
dessineDe(de3,8,340,20)
canvas.grid(row=1, column=0,columnspan=3, padx=10, pady=(10,0))        
fenetre.mainloop()

