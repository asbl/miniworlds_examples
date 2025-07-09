from miniworlds import *
import random
world = World()

@world.register
def on_setup(self):
    world.size = (200,200)

@world.register
def on_key_down_a(self):
    a = Ellipse.from_center((100, 100), 100, 100) 
    a.fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    
world.run()

