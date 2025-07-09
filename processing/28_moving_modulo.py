from miniworlds import *
import random
world = World(100,100)
c = Circle((0,50), 20)
x = 0
@world.register
def act(self):
    global x
    c.x = x % 100
    x = x + 1
world.run()