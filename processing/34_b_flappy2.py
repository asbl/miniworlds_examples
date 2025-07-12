from miniworlds import *

world = World(300, 200)

rect = Rectangle((280,120), 20, 80)
ball = Circle((20,50),20)
velocity = 1

@rect.register
def act(self):
    rect.x -= 1
    if rect.x == 0:
        rect.x = 280

@ball.register
def act(self):
    global velocity
    self.y += velocity
    if world.frame % 10 == 0:
        velocity += 1
    
world.run() 