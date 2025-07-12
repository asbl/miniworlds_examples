from miniworlds import *
import random

world = World(400, 200)
points = Number.from_topleft((0,0), 0)

red_circles = []
green_circles = []

@world.register
def act(self):
    if self.frame % 100 == 0:
        c = Circle((400, random.randint(0,200)), 40)
        c.color = (255, 0, 0)
        red_circles.append(c)
    elif self.frame % 50 == 0:
        c = Circle((400, random.randint(0,200)), 40)
        c.color = (0, 255, 0)
        green_circles.append(c)
    for circle in red_circles:
        circle.move(direction = "left")
    for circle in green_circles:
        circle.move(direction = "left")

@world.register
def on_mouse_left(self, mouse_position):
    actors = self.get_actors_from_pixel(mouse_position)
    for actor in actors:
        if actor in red_circles:
            actor.remove()
            points.set_number(points.get_number() - 1)
        elif actor in green_circles:
            actor.remove()
            points.set_number(points.get_number() + 1)
            
world.run()