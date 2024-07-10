#Author: Adwiteeya
#Date: 02/21/2024
#Purpose: Defining a city class

from cs1lib import *
from random import randint

#Window width and window height
W_W = 720
W_H = 360
number = 10000000

class City:

    def __init__(self, code, name, rgn, popn, lat, long):
        self.code = code
        self.name = name
        self.rgn = rgn
        self.popn = popn
        self.lat = lat
        self.long = long

    def __str__(self):
        return str(self.name) + "," + str(self.popn) + "," + str(self.lat) + "," + str(self.long)

    #defining draw method
    def draw(self, cx,cy):

        px = cx + self.long * (W_W/ 360)
        py = cy - self.lat * (W_H/ 180)

        #if int(self.popn) < number:
            #set_fill_color(1, 0, 0)
            #draw_circle(px, py, 3)

        #if int(self.popn) > number:
            #set_fill_color(0,1,1)
            #draw_circle(px,py,3)

        r = randint(0,1)
        g = randint(0,1)
        b = randint(0,1)

        set_fill_color(r, g, b)
        draw_circle(px, py, 3)

    def draw_text(self, cx, cy):

        px = cx + self.long * (W_W/ 360)
        py = cy - self.lat * (W_H/ 180)

        set_font_size(12)
        set_font_italic()
        draw_text(self.name, px, py)