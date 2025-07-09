from miniworlds import *
world = World(100, 100)
world.border = None
for x in range(0, 100, 10):
    for y in range(0, 100, 10):
        world.fill((x+y) * 1.4)
        world.stroke(None)
        r = Rectangle((x, y), 10, 10)
world.run()
