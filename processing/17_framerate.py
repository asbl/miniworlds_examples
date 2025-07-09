from miniworlds import *

world = World()
world.size = (120,210)

@world.register
def on_setup(self):
    world.fps = 1
    world.speed = 3
    
@world.register
def act(self):
    print(world.frame)

world.run()
