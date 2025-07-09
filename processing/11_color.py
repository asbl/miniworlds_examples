from miniworlds import *

world = World(350, 150)
r = Rectangle.from_topleft((10,10), 100, 100,)
r.fill_color = (255, 0, 0)

g = Rectangle.from_topleft((120,10), 100, 100)
g.fill_color = (0, 255,0)

b = Rectangle.from_topleft((230,10), 100, 100)
b.fill_color = (0, 0 ,255)

world.run()