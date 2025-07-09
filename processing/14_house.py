from miniworlds import *

world = World()
world.add_background((255,255,255))
world.size = (400,200)
r = Rectangle.from_topleft((10,10), 100, 100)
r.is_filled = True
r.fill_color = (255, 0, 0)
r.border = 3
r.border_color = (255, 255,0)

world.run()