from miniworlds import *

world = World()
world.size = (120,210)

@world.register
def on_setup(self):
    print(1)

print(2)

@world.register
def act(self):
    print(3)
print(4)

world.run()
