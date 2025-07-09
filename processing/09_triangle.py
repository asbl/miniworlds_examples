from miniworlds import *

world = World(800, 600)
r = Rectangle((10,10), 100, 100)

t = Triangle((100,100), (50,100), (100,30))

r.fill_color = (255, 0, 0)
t.fill_color = (255, 255, 0)
world.run()