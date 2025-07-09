from miniworlds import *
import random
world = World(100,100)
a = Rectangle((10,10),40,40)
a.fill_color = (0,0,0)
b = Rectangle((50,10),40,40)
b.fill_color = (255, 255, 255)
c = Rectangle((10,50),40,40)
c.fill_color = (255, 255, 255)
d = Rectangle((50,50),40,40)
d.fill_color = (0, 0, 0)
world.run()
