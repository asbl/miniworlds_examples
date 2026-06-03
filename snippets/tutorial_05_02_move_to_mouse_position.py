from miniworlds import *

world = World(400, 400)
world.add_background("images/grass.jpg")
player = Actor()
player.add_costume("images/player.png")
player.orientation = -90

@player.register
def act(self):
    mouse_position = self.world.mouse.get_position()
    if mouse_position:
        self.move_in_direction(mouse_position)

world.run()
