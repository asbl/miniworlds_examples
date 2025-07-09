from miniworlds import *

world = World(300, 200)

rect = Rectangle((280,120), 20, 80)

@rect.register
def act(self):
    rect.x -= 1
    if rect.x == 0:
        rect.x = 280

world.run()