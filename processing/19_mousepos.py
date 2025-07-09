from miniworlds import *

world = World()

@world.register
def act(self):
    c = Circle(world.get_mouse_position(), 40)
    c.color = (255,255,255, 100)
    c.border = None

world.run()

