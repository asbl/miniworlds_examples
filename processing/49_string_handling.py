from miniworlds import *

world = World()

text = Text((20,20), "center")
text.x = (400 - text.size[0]) / 2
print(text.size)


world.run()