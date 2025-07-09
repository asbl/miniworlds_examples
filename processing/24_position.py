from miniworlds import *
import random
world = World(100,100)

circle = Circle((50,50), 20)
x = 0

@world.register
def on_key_pressed_a(self):
    circle.x = circle.x - 1

@world.register
def on_key_pressed_d(self):
    circle.x = circle.x + 1
    

world.run()

