from miniworlds import *
world = World(100, 100)
world.border = None
for x in range(0, 100, 10):
    for y in range(0, 100, 10):
        r = Rectangle((x, y), 10, 10)
        color = int((x+y) * 1.4)
        r.color = (color, color, color)
        r.border = None
world.run()
