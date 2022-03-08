import tkinter as tk
import random as rd

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600 

x = rd.randint(0, 500)
y = rd.randint(0, 500)

def Cercle():
    canvas.create_oval(50, 150, 150, 50, fill='green')

def Carré():
    canvas.create_rectangle(50, 150, 150, 50, fill='red')

def Croix():
    canvas.create_line(50, 150, 150, 50, fill='yellow')
    canvas.create_line(50, 50, 150, 150, fill='yellow')

bouton1 = tk.Button(text="Choisir une couleur", activebackground="grey", overrelief='raised')
bouton1.grid(row=0, column=2)

bouton2 = tk.Button(text="Cercle", activebackground="grey", overrelief='raised', command=Cercle)
bouton2.grid(row=1, column=0)

bouton3 = tk.Button(text="Carré", activebackground="grey", command=Carré)
bouton3.grid(row=2, column=0)

bouton4 = tk.Button(text="Croix", activebackground="grey", command=Croix)
bouton4.grid(row=3, column=0)

canvas = tk.Canvas(background="black")
canvas.grid(row=1, column=1, rowspan=3, columnspan=4)

racine.mainloop() # Lancement de la boucle principale