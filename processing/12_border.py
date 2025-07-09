from miniworlds import *

world = World(350, 150)
r = Rectangle.from_topleft((10,10), 100, 100)
r.is_filled = False
r.border = 10
r.border_color = (0, 255,0)

world.run()