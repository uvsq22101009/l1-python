import tkinter as tk

root = tk.Tk() 
root.title("Cible.py") 
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600 
Xm, Ym = CANVAS_WIDTH/2, CANVAS_HEIGHT/2

x0, y0 = 0, 0
x1, y1 = 600, 600

n = int(input("Donner le nombre de cercles à tracer : "))

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='black')
canvas.grid()
color = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']
color_change = 0

for i in range(0, n): 
    Pi = (Xm*i)/n, (Ym*i)/n
    Qi = CANVAS_WIDTH - (Xm*i)/n, CANVAS_HEIGHT - (Ym*i)/n
    color_change = color[(i%6)]
    canvas.create_oval(Pi, Qi, fill= color_change)

root.mainloop()