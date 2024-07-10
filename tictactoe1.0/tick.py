#Author: Adwiteeya
#Date: 05/03/2024
#Purpose: Drawing tictactoe

from cs1lib import *
from random import randint
from cross import Cross
from circle import Circle


#global variables


filled_block_lol = []
new_circle_lol = []


W_X = 300
W_Y = 300
CX = W_X//2
CY = W_Y//2
start = True
zero = 0
one = 100
two = 200
three = 300
half = 50


#keys
press1 = False
press2 = False
press3 = False
press4 = False
press5 = False
press6 = False
press7 = False
press8 = False
press9 = False
press = False

#random integer for x coordinate
def randint_x():
    return randint(0, 2)

#calling randint functions
x1 = randint(0,2)
y1 = randint(0,2)

#creating a circle object
def circle_object(x1,y1):
    return Circle(x1, y1)

#drawing a cross
def draw_cross(x1,y1):
    global press, filled_block_lol
    cr1 = Cross(x1,y1)
    cr1.draw()
    filled_block_lol.append([x1,y1])

#keypress values
def mykeypress(value):
    global press, press1, press2, press3, press4, press5, press6, press7, press8, press9

    if value == "1":
        press1 = True

    if value == "2":
        press2 = True

    if value == "3":
        press3 = True

    if value == "4":
        press4 = True

    if value == "5":
        press5 = True

    if value == "6":
        press6 = True

    if value == "7":
        press7 = True

    if value == "8":
        press8 = True

    if value == "9":
        press9 = True

    if value:
        press = True

#maindraw function
def maindraw():
    clear()
    global press, start
    set_clear_color(0,0.5,0.5)
    set_stroke_color(0,0,0)

    #drawing lines for tictactoe
    draw_line(one, zero, one, three)
    draw_line(two,zero,two,three)
    set_font_bold()
    set_font_size(12)
    draw_text("Press 1-9", zero, CY+(half//2))
    draw_line(zero,one,three,one)
    draw_line(zero,two,three,two)
    draw_text("1", one - half, one - half)
    draw_text("2", two - half, one - half)
    draw_text("3", three - half, one - half)
    draw_text("4", one - half, two - half)
    draw_text("5", two - half, two - half)
    draw_text("6", three - half, two - half)
    draw_text("7", one - half, three - half)
    draw_text("8", two - half, three - half)
    draw_text("9", three - half, three - half)

    #drawing the first circle
    if start:
        draw_circlee(x1,y1)

    #drawing crosses
    if press1:
        draw_cross(0,0)
    if press2:
        draw_cross(1,0)
    if press3:
        draw_cross(2,0)
    if press4:
        draw_cross(0,1)
    if press5:
        draw_cross(1,1)
    if press6:
        draw_cross(2,1)
    if press7:
        draw_cross(0,2)
    if press8:
        draw_cross(1,2)
    if press9:
        draw_cross(2,2)

    #next circles
    if press:
        randint_update()

    for ele in new_circle_lol:  #goes over items in new_circle_lol
        if ele[2] == "c":       #this constant is just to keep drawing the circle everytime
            draw_circlee(ele[0], ele[1])

#drawing circle
def draw_circlee(x1,y1):
    global filled_block_lol
    t1 = circle_object(x1,y1)
    t1.draw()
    filled_block_lol.append([x1,y1])


#checking where to put the next circle and putting it
def randint_update():
    global press, x1, y1,new_circle_lol
    if press:
        x2 = randint(0,2)
        y2 = randint(0,2)
        press = False
        if [x2,y2] not in filled_block_lol:
            return new_circle_lol.append([x2,y2, "c"])
        else:
            press = True
            randint_update()






start_graphics(maindraw,width = W_X, height = W_Y, framerate=20, key_press = mykeypress)

