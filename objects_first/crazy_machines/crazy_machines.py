import miniworlds
import miniworlds_physics
import random

world = miniworlds_physics.PhysicsWorld(400, 400)
toolbar = world.layout.add_right(miniworlds.Toolbar(), size=200)
lines_counter = toolbar.add(miniworlds.CounterLabel("Lines"))

obj = "line"
state = None
line_dummy = None
max_length = 100

start = miniworlds.Circle((50, 50))
start.physics.simulation = None

end = miniworlds.Circle((250, 300))
end.physics.simulation = None


@end.register
def on_detecting_actor(self, other):
    if other == start:
        world.is_running = False


@world.register
def on_key_down_space(self):
    actor = miniworlds.Circle(start.center)

    @actor.register
    def act(self):
        if self.y > 400:
            self.world.stop()
            miniworlds.Text((100, 100), "You loose!")

    @actor.register
    def on_detecting(self, other):
        if other == end:
            self.world.stop()
            miniworlds.Text((100, 100), "You won!")


@world.register
def on_mouse_left_down(self, mouse_pos):
    global state
    if obj == "line" and state is None and lines_counter.get_value() < 3:
        state = mouse_pos


@world.register
def on_mouse_motion(self, mouse_pos):
    global line_dummy
    if line_dummy is not None:
        line_dummy.remove()
        line_dummy = None
    if state is not None and 0 < self.distance_to(state, mouse_pos) < max_length:
        line_dummy = miniworlds.Line(state, mouse_pos)
        line_dummy.border_color = (100, 100, 100, 100)
        line_dummy.physics.simulation = None


@world.register
def on_mouse_left_up(self, mouse_pos):
    global state
    global line_dummy
    if line_dummy is not None:
        line_dummy.remove()
        line_dummy = None
    if (
        state is not None
        and 0 < self.distance_to(state, mouse_pos) < max_length
        and lines_counter.get_value() < 3
    ):
        # Add the Line
        miniworlds.Line(state, mouse_pos)
        lines_counter.add(1)
    state = None


world.run()
