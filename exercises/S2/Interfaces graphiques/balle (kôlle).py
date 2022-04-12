import tkinter as tk
from tracemalloc import stop
# Consigne : 


##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
color_carré = ['black', 'blue']
color_rond = ['blue', 'black']
cpt = 0

###################
# Fonctions

# Balle
def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill='blue')
    return [cercle, dx, dy]

def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        cpt += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        cpt += 1

# Carré 
def creer_carre(): 
    """Dessine un carré bleu et retourne son identifiant
     et les valeur de déplacement dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    carré_def = canvas.create_rectangle((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill= 'blue')
    return [carré_def, dx, dy]

def mouvement_c():
    """Déplace le carré et ré-appelle la fonction avec un compte-à-rebours"""
    rebond_c()
    canvas.move(carré[0], carré[1], carré[2])
    canvas.after(20, mouvement_c)

def rebond_c():
    """Fait rebondir le caré sur les bords du canevas"""
    global carré, cpt
    x0, y0, x1, y1 = canvas.coords(carré[0])
    if x0 <= 0 or x1 >= 600:
        carré[1] = -carré[1]
        cpt += 1
    if y0 <= 0 or y1 >= 400:
        carré[2] = -carré[2]
        cpt +=1

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
carré = creer_carre()
balle = creer_balle()

# déplacement de la balle
if cpt <= 5 or (cpt > 10 and cpt <= 15) or (cpt>20 and cpt<=25):  
        mouvement()

if (cpt > 5 and cpt <= 10) or (cpt>15 and cpt<=20) or (cpt>25 and cpt<30): 
        mouvement_c()

if cpt >= 30: 
    pass

# boucle principale
racine.mainloop()
