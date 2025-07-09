from miniworlds import *

world = World()
world.size = (120,210)
Rectangle.from_topleft((10,100), 100, 100)
Triangle((10,100), (60, 50), (110, 100))

world.run()