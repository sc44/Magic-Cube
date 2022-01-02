#!/usr/bin/env python3

# Magic Cube - Rubik Zauberwürfel

# Programmed by Woodstock

# This program is published under the terms of the GNU General Public License.


from tkinter import Tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Label
from tkinter import IntVar
from random  import shuffle


def Anzeigen():

    i = 0
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(152+x*50, 2+y*50, 198+x*50, 48+y*50, width=3, fill=FarbListe[i]) ; i+=1
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(2+x*50, 152+y*50, 48+x*50, 198+y*50, width=3, fill=FarbListe[i]) ; i+=1
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(152+x*50, 152+y*50, 198+x*50, 198+y*50, width=3, fill=FarbListe[i]) ; i+=1
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(302+x*50, 152+y*50, 348+x*50, 198+y*50, width=3, fill=FarbListe[i]) ; i+=1
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(152+x*50, 302+y*50, 198+x*50, 348+y*50, width=3, fill=FarbListe[i]) ; i+=1
    for y in range(3):
        for x in range(3):
            Spielfeld.create_rectangle(152+x*50, 452+y*50, 198+x*50, 498+y*50, width=3, fill=FarbListe[i]) ; i+=1


def Loeschen():

    ID = Spielfeld.find_enclosed(150, 0, 300, 150)
    for i in range(len(ID)):  
        Spielfeld.delete(ID[i])
    ID = Spielfeld.find_enclosed(0, 150, 450, 300)
    for i in range(len(ID)):  
        Spielfeld.delete(ID[i])
    ID = Spielfeld.find_enclosed(150, 300, 300, 600)
    for i in range(len(ID)):  
        Spielfeld.delete(ID[i])


def Zurueck():

    if len(Letzter) > 0:
        if   Letzter[len(Letzter)-2] == 1:  Runter(Letzter[len(Letzter)-1])
        elif Letzter[len(Letzter)-2] == 2:  Hoch(Letzter[len(Letzter)-1])
        elif Letzter[len(Letzter)-2] == 3:  Rechts(Letzter[len(Letzter)-1])
        elif Letzter[len(Letzter)-2] == 4:  Links(Letzter[len(Letzter)-1])
        elif Letzter[len(Letzter)-2] == 5:  DrehenR(Letzter[len(Letzter)-1])
        elif Letzter[len(Letzter)-2] == 6:  DrehenL(Letzter[len(Letzter)-1])
        for x in range(4):
            Letzter.pop(len(Letzter)-1)
        Anzahl.set(Anzahl.get()-2)


def Hoch(a):

    for i in range(12):    # mitte vertikal
        Position[i] = Spielfeld.find_enclosed(150+a, 0+i*50, 200+a, 50+i*50)

    for i in range(3):
        Spielfeld.move(Position[i], 0, 450)
    for i in range(9):
        Spielfeld.move(Position[i+3], 0, -150)

    Letzter.append(1)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def Runter(a):

    for i in range(12):    # mitte vertikal
        Position[i] = Spielfeld.find_enclosed(150+a, 0+i*50, 200+a, 50+i*50)

    for i in range(9):
        Spielfeld.move(Position[i], 0, 150)
    for i in range(3):
        Spielfeld.move(Position[i+9], 0, -450)

    Letzter.append(2)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def Links(a):

    for i in range(9):    # mitte horizontal
        Position[i] = Spielfeld.find_enclosed(0+i*50, 150+a, 50+i*50, 200+a)
    for i in range(3):    # ganz unten
        Position[i+9] = Spielfeld.find_enclosed(150+i*50, 550-a, 200+i*50, 600-a)

    for i in range(3):
        Spielfeld.move(Position[i], 150, 400-a*2)
    for i in range(6):
        Spielfeld.move(Position[i+3], -150, 0)
    for i in range(3):
        Spielfeld.move(Position[i+9], 150, -400+a*2)

    Letzter.append(3)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def Rechts(a):

    for i in range(9):    # mitte horizontal
        Position[i] = Spielfeld.find_enclosed(0+i*50, 150+a, 50+i*50, 200+a)
    for i in range(3):    # ganz unten
        Position[i+9] = Spielfeld.find_enclosed(150+i*50, 550-a, 200+i*50, 600-a)

    for i in range(6):
        Spielfeld.move(Position[i], 150, 0)
    for i in range(3):
        Spielfeld.move(Position[i+6], -150, 400-a*2)
    for i in range(3):
        Spielfeld.move(Position[i+9], -150, -400+a*2)

    Letzter.append(4)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def DrehenL(a):

    for i in range(3):    # links
        Position[i] = Spielfeld.find_enclosed(100-a, 150+i*50, 150-a, 200+i*50)
    for i in range(3):    # unten
        Position[i+3] = Spielfeld.find_enclosed(150+i*50, 300+a, 200+i*50, 350+a)
    for i in range(3):    # rechts
        Position[i+6] = Spielfeld.find_enclosed(300+a, 250-i*50, 350+a, 300-i*50)
    for i in range(3):    # oben
        Position[i+9] = Spielfeld.find_enclosed(250-i*50, 100-a, 300-i*50, 150-a)
    Spielfeld.move(Position[0], 50+a, 150+a)
    Spielfeld.move(Position[1], 100+a, 100+a)
    Spielfeld.move(Position[2], 150+a, 50+a)
    Spielfeld.move(Position[3], 150+a, -50-a)
    Spielfeld.move(Position[4], 100+a, -100-a)
    Spielfeld.move(Position[5], 50+a, -150-a)
    Spielfeld.move(Position[6], -50-a, -150-a)
    Spielfeld.move(Position[7], -100-a, -100-a)
    Spielfeld.move(Position[8], -150-a, -50-a)
    Spielfeld.move(Position[9], -150-a, 50+a)
    Spielfeld.move(Position[10], -100-a, 100+a)
    Spielfeld.move(Position[11], -50-a, 150+a)

    Letzter.append(5)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def DrehenR(a):

    for i in range(3):    # links
        Position[i] = Spielfeld.find_enclosed(100-a, 150+i*50, 150-a, 200+i*50)
    for i in range(3):    # unten
        Position[i+3] = Spielfeld.find_enclosed(150+i*50, 300+a, 200+i*50, 350+a)
    for i in range(3):    # rechts
        Position[i+6] = Spielfeld.find_enclosed(300+a, 250-i*50, 350+a, 300-i*50)
    for i in range(3):    # oben
        Position[i+9] = Spielfeld.find_enclosed(250-i*50, 100-a, 300-i*50, 150-a)
    Spielfeld.move(Position[0], 150+a, -50-a)
    Spielfeld.move(Position[1], 100+a, -100-a)
    Spielfeld.move(Position[2], 50+a, -150-a)
    Spielfeld.move(Position[3], -50-a, -150-a)
    Spielfeld.move(Position[4], -100-a, -100-a)
    Spielfeld.move(Position[5], -150-a, -50-a)
    Spielfeld.move(Position[6], -150-a, 50+a)
    Spielfeld.move(Position[7], -100-a, 100+a)
    Spielfeld.move(Position[8], -50-a, 150+a)
    Spielfeld.move(Position[9], 50+a, 150+a)
    Spielfeld.move(Position[10], 100+a, 100+a)
    Spielfeld.move(Position[11], 150+a, 50+a)

    Letzter.append(6)
    Letzter.append(a)
    Anzahl.set(Anzahl.get()+1)


def Wuerfel():

    Spielfeld.create_polygon(343, 420, 412, 384, 481, 420, 412, 456, fill=Farbe[0])   # oben
    Spielfeld.create_line(343, 420, 412, 384, width=3)
    Spielfeld.create_line(366, 432, 435, 396, width=3)
    Spielfeld.create_line(389, 444, 458, 408, width=3)
    Spielfeld.create_line(412, 456, 481, 420, width=3)
    Spielfeld.create_line(481, 420, 412, 384, width=3)
    Spielfeld.create_line(458, 432, 389, 396, width=3)
    Spielfeld.create_line(435, 444, 366, 408, width=3)
    Spielfeld.create_line(412, 456, 343, 420, width=3)

    Spielfeld.create_polygon(343, 420, 412, 456, 412, 540, 343, 504, fill=Farbe[2])   # links
    Spielfeld.create_line(343, 420, 343, 504, width=3)
    Spielfeld.create_line(366, 432, 366, 516, width=3)
    Spielfeld.create_line(389, 444, 389, 528, width=3)
    Spielfeld.create_line(343, 448, 412, 484, width=3)
    Spielfeld.create_line(343, 476, 412, 512, width=3)
    Spielfeld.create_line(343, 504, 412, 540, width=3)

    Spielfeld.create_polygon(412, 456, 481, 420, 481, 504, 412, 540, fill=Farbe[3])   # rechts
    Spielfeld.create_line(412, 456, 412, 540, width=3)
    Spielfeld.create_line(435, 444, 435, 528, width=3)
    Spielfeld.create_line(458, 432, 458, 516, width=3)
    Spielfeld.create_line(481, 420, 481, 505, width=3)
    Spielfeld.create_line(412, 484, 481, 448, width=3)
    Spielfeld.create_line(412, 512, 481, 476, width=3)
    Spielfeld.create_line(412, 540, 481, 504, width=3)


def Neues():

    shuffle(FarbListe)
    Loeschen()
    Anzeigen()
    Anzahl.set(0)


def Reset():

    FarbListe.clear()
    for i in range(6):
        for a in range(9):
            FarbListe.append(Farbe[i]) 
    Loeschen()
    Anzeigen()
    Anzahl.set(0)



main = Tk()
main.title("Magic Cube")
main.geometry ("630x760")

Farbe = ["yellow", "orange", "blue", "red", "white", "green"]
FarbListe = []
Position = [0,0,0,0,0,0,0,0,0,0,0,0]
Letzter = []
Anzahl = IntVar()

Spielfeld = Canvas(main, width=482, height=601)
Spielfeld.place (x=90, y=80)
Wuerfel()
Reset()

Button_H1 = Button(main, bd=3, text="↑", font="Helvetica 22", command=lambda:Hoch(0))
Button_H2 = Button(main, bd=3, text="↑", font="Helvetica 22", command=lambda:Hoch(50))
Button_H3 = Button(main, bd=3, text="↑", font="Helvetica 22", command=lambda:Hoch(100))
Button_U1 = Button(main, bd=3, text="↓", font="Helvetica 22", command=lambda:Runter(0))
Button_U2 = Button(main, bd=3, text="↓", font="Helvetica 22", command=lambda:Runter(50))
Button_U3 = Button(main, bd=3, text="↓", font="Helvetica 22", command=lambda:Runter(100))
Button_L1 = Button(main, bd=3, text="←", font="Helvetica 22", command=lambda:Links(0))
Button_L2 = Button(main, bd=3, text="←", font="Helvetica 22", command=lambda:Links(50))
Button_L3 = Button(main, bd=3, text="←", font="Helvetica 22", command=lambda:Links(100))
Button_R1 = Button(main, bd=3, text="→", font="Helvetica 22", command=lambda:Rechts(0))
Button_R2 = Button(main, bd=3, text="→", font="Helvetica 22", command=lambda:Rechts(50))
Button_R3 = Button(main, bd=3, text="→", font="Helvetica 22", command=lambda:Rechts(100))
Button_D1 = Button(main, bd=3, text="↺", font="Helvetica 22", command=lambda:DrehenL(100))
Button_D2 = Button(main, bd=3, text="↺", font="Helvetica 22", command=lambda:DrehenL(50))
Button_D3 = Button(main, bd=3, text="↺", font="Helvetica 22", command=lambda:DrehenL(0))
Button_D4 = Button(main, bd=3, text="↻", font="Helvetica 22", command=lambda:DrehenR(0))
Button_D5 = Button(main, bd=3, text="↻", font="Helvetica 22", command=lambda:DrehenR(50))
Button_D6 = Button(main, bd=3, text="↻", font="Helvetica 22", command=lambda:DrehenR(100))
Anzahl_Zuege = Label(main, textvariable=str(Anzahl), relief="raised", borderwidth=3, font="Helvetica 32")
Button_Neues = Button(main, bd=3, text=" New Game ", font="Helvetica 14", command=Neues)
Button_Zurueck = Button(main, bd=3, text=" Backwards ", font="Helvetica 14", command=Zurueck)
Button_Reset = Button(main, bd=3, text=" Reset Cube ", font="Helvetica 14", command=Reset)
Button_Beenden = Button(main, bd=3, text=" Exit ", font="Helvetica 14", command=main.destroy)

Button_H1.place(x=241, y= 23, width=48, height=48)
Button_H2.place(x=291, y= 23, width=48, height=48)
Button_H3.place(x=341, y= 23, width=48, height=48)
Button_U1.place(x=242, y=692, width=48, height=48)
Button_U2.place(x=292, y=692, width=48, height=48)
Button_U3.place(x=342, y=692, width=48, height=48)
Button_L1.place(x= 30, y=232, width=48, height=48)
Button_L2.place(x= 30, y=282, width=48, height=48)
Button_L3.place(x= 30, y=332, width=48, height=48)
Button_R1.place(x=553, y=232, width=48, height=48)
Button_R2.place(x=553, y=282, width=48, height=48)
Button_R3.place(x=553, y=332, width=48, height=48)
Button_D1.place(x= 95, y= 85, width=48, height=48)
Button_D2.place(x=143, y=133, width=48, height=48)
Button_D3.place(x=191, y=181, width=48, height=48)
Button_D4.place(x=392, y=181, width=48, height=48)
Button_D5.place(x=440, y=133, width=48, height=48)
Button_D6.place(x=488, y= 85, width=48, height=48)
Anzahl_Zuege.place(x=50, y=418, width=150,height=60)
Button_Neues.place(x=50, y=490, width=150, height=40)
Button_Zurueck.place(x=50, y=540, width=150, height=40)
Button_Reset.place(x=50, y=590, width=150, height=40)
Button_Beenden.place(x=50, y=640, width=150, height=40)


main.mainloop()

