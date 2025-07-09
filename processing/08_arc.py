from miniworlds import *

world = World(800, 600)
a1 = Arc.from_center((200, 200), 200, 200, 30, 242)
a1.border = 4
world.run()