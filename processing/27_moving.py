from miniworlds import *
import random
world = World(100,100)
c = Circle((0,50), 20)
@world.register
def act(self):
    c.x = c.x + 1
    
world.run()