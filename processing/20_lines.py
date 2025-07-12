from miniworlds import *

world = World()

@world.register
def on_setup(self):
    world.size = (200,200)

@world.register
def act(self):
    Line(world.mouse.get_last_position(), world.mouse.get_position()) 

world.run()

