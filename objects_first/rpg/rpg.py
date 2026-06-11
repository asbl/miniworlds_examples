from miniworlds import (
    TiledWorld,
    Toolbar,
    Console,
    Actor,
    Button,
    Label,
    PagerHorizontal,
    YesNoButton,
)

world = TiledWorld()
world.columns = 8
world.rows = 8
world.tile_size = 24
world.camera.world_size_x = 16
world.camera.world_size_y = 16
world.add_background((255, 255, 255, 255))
world.tick_rate = 1

toolbar = Toolbar()
@toolbar.register
def on_setup(self):
    self.add_background("images/bg")
    self.background.set_mode(mode="textured", texture_size=(200, 200))

world.toolbar = world.layout.add_right(toolbar, size=180)

console = Console()
world.console = world.layout.add_bottom(console, size=100)
world.console.newline("You enter a new world")

pager = PagerHorizontal(console)
world.layout.add_bottom(pager, size=60)

pending_question = None
question_widgets = []


def clear_question():
    global pending_question
    for widget in question_widgets:
        world.toolbar.remove(widget)
    question_widgets.clear()
    pending_question = None


def ask_yes_no(message, on_yes, on_no=None):
    global pending_question
    if pending_question is not None:
        return
    world.console.newline(message)
    label = Label(message)
    buttons = YesNoButton("Yes", "No")
    world.toolbar.add(label)
    world.toolbar.add(buttons)
    question_widgets.extend([label, buttons])
    pending_question = {"Yes": on_yes, "No": on_no}


@world.register
def on_message(self, message):
    if pending_question is not None and message in pending_question:
        callback = pending_question[message]
        clear_question()
        if callback:
            callback()

def create_grass(pos):
    g = Actor(pos)
    g.add_costume("images/grass2.png")
    g.static = True
    g.layer = 0


def create_wall(pos, walls):
    w = Actor(pos)
    w.add_costume("images/wall.png")
    w.static = True
    w.is_blocking = True
    walls.append(w)


@world.register
def on_setup(self):
    for i in range(world.rows):
        for j in range(world.columns):
            create_grass((j, i))
    self.walls = []
    create_wall((0, 4), self.walls)
    create_wall((1, 4), self.walls)
    create_wall((2, 4), self.walls)
    create_wall((3, 4), self.walls)
    create_wall((4, 4), self.walls)
    create_wall((5, 4), self.walls)
    create_wall((6, 4), self.walls)
    create_wall((6, 0), self.walls)
    create_wall((6, 1), self.walls)
    create_wall((6, 3), self.walls)
    self.music.play("sounds/bensound-betterdays.mp3")
    

torch = Actor((10, 4))


@torch.register
def on_setup(self):
    torch.layer = 2
    torch.add_costume("images/torch.png")


fireplace = Actor((10, 12))
fireplace.layer = 2


@fireplace.register
def on_setup(self):
    self.costume_not_burned = fireplace.add_costume("images/fireplace_0.png")
    self.burning = False
    self.costume_burned = fireplace.add_costume(
        ["images/fireplace_1.png", "images/fireplace_2.png"]
    )
    fireplace.switch_costume(self.costume_not_burned)


door = Actor((6, 2))

@door.register
def on_setup(self):
    self.add_costume("images/door_closed.png")
    self.closed = True
    self.door_open_costume = door.add_costume("images/door_open.png")
    self.switch_costume(0)
    door.layer = 2


player = Actor((8, 2))


@player.register
def on_setup(self):
    self.add_costume("images/knight")
    self.costume.is_rotatable = False
    self.layer = 3
    self.is_blockable = True


@player.register
def act(self):
    self.world.camera.from_actor(self)



@player.register_message("burn")
def burn_torch(self, sender):
    print("BURN?")
    if not fireplace.burning:
        fireplace.world.sound.play("sounds/fireplace.wav")
        fireplace.switch_costume(fireplace.costume_burned)
        fireplace.costume.is_animated = True


@player.register_message("open_door")
def open(self, sender):
    if door.closed:
        door.switch_costume(door.door_open_costume)
        door.world.sound.play("sounds/olddoor.wav")
        door.closed = False


inventory = []
torch_button = None


@player.register
def on_key_down_w(self):
    if pending_question is None:
        player.move_in_direction("up")


@player.register
def on_key_down_s(self):
    if pending_question is None:
        player.move_in_direction("down")


@player.register
def on_key_down_a(self):
    if pending_question is None:
        player.move_in_direction("left")


@player.register
def on_key_down_d(self):
    if pending_question is None:
        player.move_in_direction("right")


@player.register_message("Torch")
def light_fireplace(self, data):
    global torch_button
    print("light")
    found_actors = player.detect_all()
    if fireplace in found_actors:
        self.world.console.newline("You light the fireplace.")
        self.send_message("burn")
        if torch_button is not None:
            self.world.toolbar.remove(torch_button)
            torch_button = None
    else:
        self.world.console.newline("...nothing happens")


@player.register_sensor(door)
def ask_open_door(self, door):
    if door.closed:
        self.undo_move()
        message = "The door is closed - Do you want to open it?"
        ask_yes_no(message, lambda: self.send_message("open_door"))


@player.register_sensor(torch)
def pick_up_torch(self, torch):
    def pick_up():
        global torch_button
        inventory.append("Torch")
        torch.remove()
        l = Label("You pick up the torch")
        world.console.add(l)
        
        torch_button = Button("Torch", "images/torch.png")
        world.toolbar.add(torch_button)

    ask_yes_no("You find a torch - Do you want to pick it up?", pick_up)


world.run()
