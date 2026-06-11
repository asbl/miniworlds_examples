import miniworlds


world = miniworlds.World(560, 360)
world.background = (236, 241, 246)

status = miniworlds.Text((24, 24), "Click a button to open a dialog.")
status.origin = "topleft"
status.font_size = 20

click_area = miniworlds.Rectangle.from_topleft((260, 78), 250, 210)
click_area.fill_color = (214, 226, 238)
click_area.border_color = (82, 100, 120)

click_count = 0
click_label = miniworlds.Text((284, 165), "World clicks: 0")
click_label.origin = "topleft"
click_label.font_size = 24


def set_status(text):
    status.text = text


def make_button(position, label, callback):
    button = miniworlds.Rectangle.from_topleft(position, 190, 44)
    button.fill_color = (63, 93, 132)
    button.border_color = (34, 48, 68)

    text = miniworlds.Text((position[0] + 16, position[1] + 12), label)
    text.origin = "topleft"
    text.font_size = 20
    text.color = (255, 255, 255)

    @button.register
    def on_clicked_left(self, mouse_pos):
        callback()

    @text.register
    def on_clicked_left(self, mouse_pos):
        callback()

    return button


def show_yes_no():
    world.dialog.ynbox(
        "Do you want to continue?",
        "Question",
        callback=lambda value: set_status(f"Yes-No result: {value}"),
    )


def show_choice():
    world.dialog.choicebox(
        "Choose your next color.",
        "Choice",
        choices=["Red", "Green", "Blue", "Yellow"],
        callback=lambda value: set_status(f"Choice result: {value}"),
    )


def show_input():
    world.dialog.enterbox(
        "What is your name?",
        "Input",
        default="Ada",
        callback=lambda value: set_status(f"Input result: {value}"),
    )


make_button((36, 88), "Yes / No", show_yes_no)
make_button((36, 150), "Choice", show_choice)
make_button((36, 212), "Input", show_input)


@click_area.register
def on_clicked_left(self, mouse_pos):
    global click_count
    click_count += 1
    click_label.text = f"World clicks: {click_count}"


world.run()
