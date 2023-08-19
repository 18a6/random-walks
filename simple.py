import random
from tkinter import *

class Walker():
    def __init__(self, x, y, walk_max_length):
        """x and y are floats, initial position of the walker"""
        self.x = x
        self.y = y
        self.walk_max_length = walk_max_length

    def walk(self):
        self.x += random.randint(-1 * self.walk_max_length, self.walk_max_length)
        self.y += random.randint(-1 * self.walk_max_length, self.walk_max_length)
        return self.x, self.y

class Plain():
    def __init__(self, width, height):
        """width and height are int > 0, width and heigth of the plain"""
        self.width = width
        self.height = height
 
    def draw_point(self, canvas, x, y):
        point_radius = 1
        canvas.create_oval(x - point_radius, y - point_radius, x + point_radius, y + point_radius, fill="black")

    def update_walker_position(self, canvas, walker, pace):
        x, y = walker.walk()
        self.draw_point(canvas, x, y)
        canvas.after(pace, self.update_walker_position, canvas, walker, pace)

    def simulate(self, max_walk_length, pace):
        """max_walk_length is int, speed is int > 0"""
        root = Tk()
        half_width, half_height = self.width, self.height
        canvas = Canvas(root, width=half_width*2, height=half_height*2)
        canvas.pack()

        walker = Walker(half_width, half_height, max_walk_length)
        self.draw_point(canvas, half_width, half_height)
        self.update_walker_position(canvas, walker, pace)

        root.mainloop()

plain = Plain(500, 500)
plain.simulate(5, 1)