

from cs1lib import *

class Cross:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)




    def draw(self):
        set_stroke_width(10)
        set_stroke_color(0.5, 0, 0)
        draw_line(100 * self.x, 100 * self.y, 100 * self.x+100, 100 * self.y+100)
        draw_line(100 * self.x + 100, 100 * self.y, 100 * self.x, 100 * self.y + 100)