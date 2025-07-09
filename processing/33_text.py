from miniworlds import *

world = World()
world.size = (600,300)

text = Text.from_topleft((200,100), "Hello World")
text.border = 1
text.font_size = 100
text.direction = 5
world.run()