#Author: Adwiteeya
#Date: 02/21/2024
#Purpose: Driving the city file

from cs1lib import *
from city import City
from quicksort import sort
from random import randint

apress = False
bpress = False
kpress = False
trueanswer = False
falseanswer = False
start = False
pstart = True
#window width and window height
W_W = 720
W_H = 360

#center of window width and window height
CX = W_W/2
CY = W_H/2

city_list = []

def reading_file(file_name):
#opening for reading file
    fp_r = open(file_name, "r")

#processing file

    for line in fp_r:                       #goes over lines in the file
        line_strip = line.strip()
        line_split= line_strip.split(",")

        c1 = City(line_split[0], line_split[1], line_split[2], int(line_split[3]), float(line_split[4]), float(line_split[5]))
        city_list.append(c1)

    #closing for reading file
    fp_r.close()
    return city_list

def writing_file(file_name, city_list):
#closing for writing file
    fp_w = open(file_name, "w")

    for city in city_list:
        info = str(city) + "\n"
        fp_w.write(info)

    fp_w.close()

#loading image
img = load_image("world.png")

def if_answer():
    draw_text("Congrats!", CX, CY-10)

def if_not_answer():
    draw_text("Oops, not quite!", CX, CY-10)


#function to compare cities
def compare_alpha(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# function to compare population
def compare_population(city1, city2):
    return city1.popn >= city2.popn

# function to compare latitude
def compare_latitude(city1, city2):
    return city1.lat <= city2.lat

i = randint(0,600)

def my_keypress(value):
    global apress, bpress, kpress, i, start, pstart, trueanswer, falseanswer
    if value == "a":
        apress = True
    if value == "b":
        bpress = True
    if value == "p":
        apress = False
        bpress = False
        pstart = False
        trueanswer = False
        falseanswer = False
        i = i + 100
        start = True

#maindraw function
def maindraw():
    global apress, bpress, kpress, trueanswer, start, falseanswer

    draw_image(img, 0, 0)


    if pstart:
        draw_text("Press p to start", CX, CY)

    if start and not trueanswer and not falseanswer:
        city_list[i].draw(CX, CY)
        set_font_normal()
        set_font_size(18)
        if str(city_list[i].name) < str(city_list[i-10].name):
            draw_text("What city is this? a) " + str(city_list[i].name) + " b) " + str(city_list[i-10].name), CX-100, CY+100)
            draw_text("Press a or b!", CX, CY + 30)
            if apress == True:
                trueanswer = True
            if bpress == True:
                falseanswer = True


        else:
            draw_text("What city is this? a) " + str(city_list[i-10].name) +  " b) " + str(city_list[i].name), CX-100, CY+100)
            draw_text("Press a or b!", CX, CY + 30)
            if bpress == True:
                trueanswer = True
            if apress == True:
                falseanswer = True



    if trueanswer:
        city_list[i].draw(CX, CY)
        set_font_normal()
        set_font_size(18)
        city_list[i].draw_text(CX, CY)
        draw_text("Congrats!! Press p to play again!", CX, CY + 80)

    if falseanswer:
        city_list[i].draw(CX, CY)
        set_font_normal()
        set_font_size(18)
        city_list[i].draw_text(CX, CY)
        draw_text("Oops, not quite right! Press p to play again!", CX, CY + 80)


#calling sort function for names
clist = reading_file("world_cities.txt")
sort(clist, compare_alpha)
writing_file("cities_alpha.txt", clist)

#calling sort function for latitude
sort(clist, compare_latitude)
writing_file("cities_latitude.txt", clist)

#calling sort function for population
sort(clist, compare_population)
writing_file("cities_population.txt", clist)

start_graphics(maindraw, width = W_W, height = W_H, framerate = 20, key_press=my_keypress)
