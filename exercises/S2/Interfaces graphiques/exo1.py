# Consignes : 
# 1 - Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
# 2 - Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
# 3 - A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
# 4 - Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
# 5 - A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné.
###########################


import tkinter as tk

# variable qui permet de choisir la couleur du rectangle
couleur = 0

# dit si  la couleur est  fixe
est_fixe = False

# coordonnées des sommets du rectangle:
x1, y1 = 150, 150
x2, y2 = 350, 350


#fonctions
def gestion_clic(event):
    """ Gère le clic sur le canevas"""
    global couleur, est_fixe
    if est_fixe:
        return
    liste_couleurs = ["red", "blue"]
    if x1 < event.x < x2 and y1 < event.y < y2:
        couleur = 1 - couleur
        canvas.itemconfigure(rectangle, fill=liste_couleurs[couleur])
    else:
        est_fixe = True


def restart():
    """Met le rectangle à rouge et autorise à modifier la couleur"""
    global couleur, est_fixe
    est_fixe = False
    couleur = 0
    canvas.itemconfigure(rectangle, fill="red")


#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=500, height=500)
bouton = tk.Button(racine, text="Recommencer", command=restart)

#positionnement des widgets
canvas.grid()
bouton.grid()

#dessin d'un rectangle rouge
rectangle = canvas.create_rectangle((x1, y1), (x2, y2), fill="red")

#liaison du clic
canvas.bind("<Button-1>", gestion_clic)

#boucle principale
racine.mainloop()