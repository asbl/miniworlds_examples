from miniworlds import *
world = World()

mover = Circle()
mover.velocity = Vector(0, 0)
mover.topspeed = 10


@world.register
def act(self):
    mouse_vec = Vector(world.mouse.x(), world.mouse.y())
    location = Vector.from_actor_position(mover)
    acceleration = mouse_vec - location
    acceleration.normalize().multiply(2)
    mover.velocity.add(acceleration)
    mover.velocity.limit(mover.topspeed)
    mover.move_vector(mover.velocity)
        
world.run()
