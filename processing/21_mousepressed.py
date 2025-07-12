from miniworlds import *

world = World()

@world.register
def on_setup(self):
    world.size = (200,200)

@world.register
def act(self):
    Ellipse(world.mouse.get_position(), 10, 10) 

@world.register
def on_mouse_left(self, position):
    world.fill_color = (255, 0, 0)
    
@world.register
def on_mouse_right(self, position):
    world.fill_color = (255, 255, 255)
    
world.run()

