from miniworlds import *
world = World(100,100)
a = 3
@world.register
def on_key_pressed_a(self):
    print(a)
world.run()


