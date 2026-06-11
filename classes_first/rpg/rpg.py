import miniworlds

class MyWorld(miniworlds.TiledWorld):

    def on_setup(self):
        self.pending_question = None
        self.question_widgets = []
        self.torch_button = None
        self.columns = 24
        self.rows = 14
        self.tile_size = 20
        self.add_background((255,255,255,255))
        for i in range(self.rows):
            for j in range(self.columns):
                g = Grass((j, i))
                g.static = True
        Wall((0, 4))
        Wall((1, 4))
        Wall((2, 4))
        Wall((3, 4))
        Wall((4, 4))
        Wall((5, 4))
        Wall((6, 4))
        Wall((6, 0))
        Wall((6, 1))
        Wall((6, 3))
        self.torch = Torch((10, 4))
        self.fireplace = Fireplace((10, 12))
        self.door = Door((6, 2))
        self.player = Player((8, 2))
        self.music.play("sounds/bensound-betterdays.mp3")
        self.toolbar = miniworlds.Toolbar()
        self.console = miniworlds.Console()
        self.toolbar = self.layout.add_right(self.toolbar, size = 200)
        self.console = self.layout.add_bottom(self.console, size = 100)

    def on_message(self, data):
        if self.pending_question is not None and data in self.pending_question:
            callback = self.pending_question[data]
            self.clear_question()
            if callback:
                callback()
            return

        if data == "Fackel":
            fireplace = self.player.detect(Fireplace)
            if fireplace:
                self.console.newline("Du zündest die Feuerstelle an.")
                self.fireplace.burn()
                if self.torch_button is not None:
                    self.toolbar.remove(self.torch_button)
                    self.torch_button = None

    def ask_yes_no(self, message, on_yes, on_no=None):
        if self.pending_question is not None:
            return
        self.console.newline(message)
        label = miniworlds.Label(message)
        buttons = miniworlds.YesNoButton("Ja", "Nein")
        self.toolbar.add(label)
        self.toolbar.add(buttons)
        self.question_widgets.extend([label, buttons])
        self.pending_question = {"Ja": on_yes, "Nein": on_no}

    def clear_question(self):
        for widget in self.question_widgets:
            self.toolbar.remove(widget)
        self.question_widgets.clear()
        self.pending_question = None


class Player(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/knight.png")
        self.costume.is_rotatable = False
        self.inventory = []
        self.is_blockable = True

    def on_key_down_w(self):
        if self.world.pending_question is None:
            self.move_in_direction("up")

    def on_key_down_s(self):
        if self.world.pending_question is None:
            self.move_in_direction("down")

    def on_key_down_a(self):
        if self.world.pending_question is None:
            self.move_in_direction("left")

    def on_key_down_d(self):
        if self.world.pending_question is None:
            self.move_in_direction("right")

    def on_detecting_torch(self, torch):
        def pick_up():
            self.inventory.append("Torch")
            self.world.torch.remove()
            self.world.console.newline("Du hebst die Fackel auf.")
            self.world.torch_button = miniworlds.Button("Fackel", "images/torch.png")
            self.world.toolbar.add(self.world.torch_button)

        self.world.ask_yes_no(
            "Du findest eine Fackel. Möchtest du sie aufheben?",
            pick_up,
        )

    def on_detecting_wall(self, wall):
        self.undo_move()

    def on_detecting_door(self, door):
        if door.closed:
            self.undo_move()
            message = "Die Tür ist geschlossen... möchtest du sie öffnen"
            def open_door():
                self.world.door.open()
                self.world.console.newline("Du hast das Tor geöffnet.")
            self.world.ask_yes_no(message, open_door)
        else:
            self.world.console.newline("Du gehst durch das Tor...")

class Wall(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/wall.png")
        self.static = True
        self.is_blocking = True


class Grass(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/grass.png")
        self.static = True

class Torch(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/torch.png")


class Fireplace(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/fireplace_0.png")
        self.costume_burned = self.add_costume(["images/fireplace_1.png", "images/fireplace_2.png"])
        self.burning = False

    def burn(self):
        if not self.burning:
            self.world.play_sound("sounds/fireplace.wav")
            self.switch_costume(self.costume_burned)
            self.costume.is_animated = True


class Door(miniworlds.Actor):

    def on_setup(self):
        self.add_costume("images/door_closed.png")
        self.costume_open = self.add_costume("images/door_open.png")
        self.closed = True

    def open(self):
        if self.closed:
            self.switch_costume(self.costume_open)
            #self.world.play_sound("sounds/olddoor.wav")
            self.closed = False


myworld = MyWorld()
myworld.run()
