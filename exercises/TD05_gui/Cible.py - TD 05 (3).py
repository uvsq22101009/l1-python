import tkinter as tk 

root = tk.Tk() 
root.title("Cible.py") 
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600 

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='black')
canvas.grid()

canvas.create_oval(0, 0, 600, 600, fill='blue')
canvas.create_oval(10, 10, 590, 590, fill='green')
canvas.create_oval(20, 20, 580, 580, fill='white')
canvas.create_oval(30, 30, 570, 570, fill='yellow')
canvas.create_oval(40, 40, 560, 560, fill='magenta')
canvas.create_oval(50, 50, 550, 550, fill='red')

root.mainloop() 

# Input un nombre (n) de cercle 
# Diviser 300 par n pour obtenir les Pi

