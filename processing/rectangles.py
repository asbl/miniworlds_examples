from miniworlds import *
world = World(100, 100)
world.border = None
for x in range(0, 100, 10):
    for y in range(0, 100, 10):
        r = Rectangle((x, y), 10, 10)
        r.color = (x+y) * 1.4
        r.border = None
world.run()