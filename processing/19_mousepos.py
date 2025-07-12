from miniworlds import *

world = World()

@world.register
def act(self):
    print("act::", self.mouse.position)
    c = Circle(self.mouse.position, 40)
    c.color = (255,255,255, 100)
    c.border = None

world.run()

