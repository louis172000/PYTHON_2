import turtle as tu
import math
from time import sleep

# coin haut gauche = -960,540

# tu.title('projet')
screen = tu.Screen()
screen.setup(width=1920, height=1080, startx=0, starty=0)

lignes = tu.Turtle()
lignes.ht()
lignes.speed(0)
lignes.width(1)
note = tu.Turtle()
note.speed(0)
note.width(0.5)
note.ht()
hampe = tu.Turtle()
hampe.width(2)
hampe.ht()

global cx
global cy
cx = -910
cy = 440
global compteur
compteur = 0
global liste_type
liste_type = []
global retourligne
retourligne = 0



def page(cx, cy):
    cx -= 50
    cy -= -100
    lignes.up()
    lignes.goto(0, 540)
    lignes.down()
    lignes.goto(0, -540)
    for l in [0, 960]:
        for n in range(0, 9):
            for i in range(0, 5):
                lignes.up()
                lignes.goto(cx+40+l, cy-70-i*10-n*110)                                 # une ligne = intervalle de 10
                lignes.down()
                lignes.goto(cx+890+l, cy-70-i*10-n*110)


def notes(style):
    global cx
    global cy
    fin_de_mesure()
    note.up()
    hauteurnote = 0
    if style == "k" or style == "s" or style == "a" or style == "m" or style == "b":                                 # elipse
        if style == "k":
            hauteurnote = -20
        if style == "s":
            hauteurnote = +10
        if style == "a":
            hauteurnote = +25
        if style == "m":
            hauteurnote = +20
        if style == "b":
            hauteurnote = -10
        note.goto(cx, cy+hauteurnote)
        note.down()
        note.left(-25)
        note.begin_fill()
        for loop in range(2):       # Draws 2 halves of ellipse
            note.circle(7, 90)      # Long curved part
            note.circle(7/2, 90)
        note.end_fill()
        note.left(25)               # la base de la hampe est dans le haut gauche de l'élipse
        draw_hampes_bot()
        type_barre_bot()
    if style == "x" or style == "c" or style == "r":                                                           # cross
        if style == "x":
            hauteurnote = +40
        if style == "c":
            hauteurnote = +50
        if style == "r":
            hauteurnote = +35
        note.goto(cx, cy+hauteurnote)
        note.down()
        note.width(1.5)
        note.left(-45)
        note.forward(math.sqrt(200))
        note.up()
        note.left(45)
        note.backward(10)
        note.left(45)
        note.down()
        note.forward(math.sqrt(200))
        note.width(0.5)
        note.up()
        note.left(-45)
        note.backward(10)
        if style == "c":                            #
            note.left(-90)
            note.forward(10)
            note.left(90)
            note.backward(2)
            note.width(1)
            note.down()
            note.forward(15)
            note.width(0.5)
            note.up()
            note.backward(12)
        draw_hampes_top()
        type_barre_top()


def type_barre_top():
    global liste_type
    # print("listetype top = ", liste_type)
    if liste_type == [1, 0, 1]:
        simple_barre_top()
    if liste_type == [1, 1, 1, 1]:
        double_barre_top()
    if liste_type == [0, 0, 1]:
        croche_seule_top()


def type_barre_bot():
    global liste_type
    # print("listetype bot = ", liste_type)
    if liste_type == [1, 0, 1]:
        simple_barre_bot()
    if liste_type == [1, 1, 1, 1]:
        double_barre_bot()
    if liste_type == [0, 0, 1]:
        croche_seule_bot()


def croche_seule_top():
    global cx
    global cy
    hampe.down()                    # croche est formée de deux cercles de rayon différents en jouant sur l'épaisseur
    hampe.left(180+95)
    hampe.width(4)
    hampe.circle(16, 30)
    hampe.width(4)
    hampe.circle(16, 10)
    hampe.width(3)
    hampe.circle(-18, 20)
    hampe.width(2)
    hampe.circle(-18, 10)
    hampe.width(1.5)
    hampe.circle(-18, 30)           # il faut dessiner le silence et faire le meme programme pour la croche bot
    hampe.setheading(0)             # permet d'orienter le racer comme en position initiale
    hampe.up()
    hampe.backward(40)
    hampe.dot(5)
    hampe.down()
    hampe.forward(8)
    hampe.right(120)
    hampe.circle(20, 45)
    hampe.up()
    hampe.circle(20, -45)

    hampe.right(-120)


def croche_seule_bot():
    global cx
    global cy
    hampe.down()                    # croche est formée de deux cercles de rayon différents en jouant sur l'épaisseur
    hampe.left(95)
    hampe.width(4)
    hampe.circle(16, 30)
    hampe.width(4)
    hampe.circle(16, 10)
    hampe.width(3)
    hampe.circle(-18, 20)
    hampe.width(2)
    hampe.circle(-18, 10)
    hampe.width(1.5)
    hampe.circle(-18, 30)           # il faut dessiner le silence et faire le meme programme pour la croche bot
    hampe.setheading(0)             # permet d'orienter le racer comme en position initiale*
    hampe.up()
    hampe.backward(15)
    hampe.dot(5)
    hampe.down()
    hampe.forward(8)
    hampe.right(120)
    hampe.circle(20, 45)
    hampe.up()
    hampe.circle(20, -45)

    hampe.right(-120)


def draw_hampes_top():
    notex, notey = note.pos()
    hampe.up()
    hampe.goto(notex+10, notey+1)
    hampe.down()
    hampe.left(90)
    hampe.forward(30)
    hampe.left(-90)
    hampe.up()


def draw_hampes_bot():
    notex, notey = note.pos()
    hampe.up()
    hampe.goto(notex-1, notey+1)
    hampe.down()
    hampe.left(-90)
    hampe.forward(30)
    hampe.left(90)
    hampe.up()


def fin_de_mesure():
    global cx
    global cy
    global compteur
    global retourligne
    if compteur % (13*4*4) == 0:
        note.up()
        note.goto(cx+12, cy+30)
        note.down()
        note.goto(cx+12, cy-10)

def retour_a_la_ligne():
    global cx
    global cy
    global compteur
    global retourligne
    if retourligne == 31:
        cx -= compteur
        compteur = 0
        cy -= 110




def simple_barre_top():
    global cx
    global cy
    hampe.left(180)
    hampe.down()
    hampe.width(3)
    hampe.forward(13*2)
    hampe.width(2)
    hampe.up()
    hampe.left(-180)
    hampe.backward(13*2)


def simple_barre_bot():
    global cx
    global cy
    hampe.left(180)
    hampe.down()
    hampe.width(3)
    hampe.forward(13*2)
    hampe.width(2)
    hampe.up()
    hampe.left(-180)
    hampe.backward(13*2)


def double_barre_top():
    global cx
    global cy
    hampe.left(180)
    hampe.down()
    hampe.width(4)
    hampe.forward(13*3)
    hampe.width(2)
    hampe.up()
    hampe.left(90)
    hampe.forward(7)
    hampe.left(90)
    hampe.down()
    hampe.forward(13*3)


def double_barre_bot():
    global cx
    global cy
    hampe.left(180)
    hampe.down()
    hampe.width(4)
    hampe.forward(13*3)
    hampe.width(2)
    hampe.up()
    hampe.left(-90)
    hampe.forward(7)
    hampe.left(-90)
    hampe.down()
    hampe.forward(13*3)


def lecture_text():
    with open("data.txt", "r") as fichier:
        liste_note = fichier.read().split(" " or "\n")
        # print(liste_note)
        return liste_note


def mainloop():
    global cx
    global cy
    global compteur
    global liste_type
    global retourligne
    screen.delay(0)
    liste = lecture_text()                                      # la liste est de la forme ["xxxx", "----", "xxxx\n----"
    for i in range(0, len(liste)):                              # parcour toute la liste
        #  #########retourligne += 1
        for l in range(0, len(liste[i])):                       # parcour la serie "xxxx" or "----\n----"
            item = liste[i]
            # print(item[l])
            if item[l] == "\n":                                 # retour à la ligne grace au compteur
                    cx -= compteur
                    compteur = 0
                    liste_type.clear()
            elif item[l] is not " ":                            # dessin de la note
                if item[l] is not "-":
                    liste_type.append(1)
                else:
                    liste_type.append(0)

                #print(liste_type)
                cx += 13
                compteur += 13
                notes(item[l])
        print(retourligne)
        liste_type.clear()
        retour_a_la_ligne()                                     # retourne à la ligne à la fin d'un bloc de 4 xxxx













# tu.tracer(0, 0)

# ---------------------------------- main prog --------------------------------------------#
screen.delay(0)
page(cx, cy)
lecture_text()
cx -= 5
mainloop()

# notes("hhc")
#     notes("t1")
#     cx += 15
#     compteur += 15
#
#     notes("hhc")
#     notes("t2")
#     cx += 15
#     compteur += 15
#
#     notes("hhc")
#     notes("t3")
#     cx += 15
#     compteur += 15
#
#     notes("hhc")
#     double_barre()
#     notes("k")
#     cx += 15
#     compteur += 15
#
#     notes("s")
#     cx += 15
#     compteur += 15
#


screen.exitonclick()
