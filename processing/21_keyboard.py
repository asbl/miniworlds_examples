from miniworlds import *

world = World()

@world.register
def on_setup(self):
    world.size = (200,200)

@world.register
def on_key_down_a(self):
    a = Ellipse.from_center((100, 100), 100, 100) 
    a.fill_color = (255, 0, 0)

@world.register
def on_key_down_b(self):
    a = Ellipse.from_center((100, 100), 100, 100) 
    a.fill_color = (0, 255, 0)

    
world.run()

