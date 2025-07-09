from miniworlds import *

world = World()
world.size = (120,210)

@world.register
def on_setup(self):
    print("setup")
    
@world.register
def act(self):
    print("act")

world.run()
