from miniworlds import *

world = World(200, 200)

for i in range(4):
    Circle((20 + 50 * i, 50), 20)
    
world.run()
