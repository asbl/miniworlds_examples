from miniworlds import *

world = World()

@world.register
def on_setup(self):
    world.size = (200,200)

@world.register
def act(self):
    Line(world.get_prev_mouse_position(), world.get_mouse_position()) 

world.run()

