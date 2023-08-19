import random

class walker():
    def __init__(self, x, y):
        """x and y are floats, inittial position of the walker"""
        self.x = x
        self.y = y 

    def walk(self):
        self.x += random.choice(-1, 1) * random.random
        self.y += random.choice(-1, 1) * random.random


def simulate():
    w = walker(0, 0)
    w.walk()
    
simulate()