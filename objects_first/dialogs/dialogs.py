import miniworlds


world = miniworlds.World(620, 380)

status = miniworlds.Text((24, 24), "Start the dialog sequence.")
status.origin = "topleft"
status.font_size = 20

click_area = miniworlds.Rectangle.from_topleft((320, 88), 250, 210)
click_area.fill_color = (214, 226, 238)
click_area.border_color = (82, 100, 120)

click_count = 0
click_label = miniworlds.Text((344, 175), "World clicks: 0")
click_label.origin = "topleft"
click_label.font_size = 24

summary = miniworlds.Text((24, 330), " ")
summary.origin = "topleft"
summary.font_size = 18

dialog_data = {
    "name": "",
    "color": "",
}


def set_status(text):
    status.text = text


def make_button(position, label, callback):
    button = miniworlds.Rectangle.from_topleft(position, 230, 44)
    button.fill_color = (63, 93, 132)
    button.border_color = (34, 48, 68)

    text = miniworlds.Text((position[0] + 16, position[1] + 12), label)
    text.origin = "topleft"
    text.font_size = 20
    text.color = (255, 255, 255)

    @button.register
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


def start_dialog_sequence():
    set_status("Sequence started.")
    summary.text = " "
    dialog_data["name"] = ""
    dialog_data["color"] = ""
    world.dialog.ynbox(
        "Do you want to configure a player?",
        "Start",
        callback=handle_start_choice,
    )


def handle_start_choice(value):
    if not value:
        set_status("Sequence cancelled.")
        return
    world.dialog.enterbox(
        "What is the player's name?",
        "Player",
        default="Ada",
        callback=handle_name,
    )


def handle_name(value):
    if value is None:
        set_status("Name input cancelled.")
        return
    dialog_data["name"] = value
    world.dialog.choicebox(
        f"Choose a color for {value}.",
        "Color",
        choices=[
            "Red",
            "Green",
            "Blue",
            "Yellow",
            "Purple",
            "Orange",
            "Cyan",
            "Pink",
            "White",
            "Black",
        ],
        callback=handle_color,
    )


def handle_color(value):
    if value is None:
        set_status("Color selection cancelled.")
        return
    dialog_data["color"] = value
    world.dialog.ynbox(
        f"Create {dialog_data['name']} with color {value}?",
        "Confirm",
        callback=handle_confirmation,
    )


def handle_confirmation(value):
    if value:
        set_status("Sequence completed.")
        summary.text = f"Player: {dialog_data['name']} | Color: {dialog_data['color']}"
    else:
        set_status("Sequence cancelled at confirmation.")
        summary.text = " "


make_button((36, 88), "Dialog sequence", start_dialog_sequence)
make_button((36, 150), "Yes / No only", show_yes_no)
make_button((36, 212), "Choice only", show_choice)
make_button((36, 274), "Input only", show_input)


@click_area.register
def on_clicked_left(self, mouse_pos):
    global click_count
    click_count += 1
    click_label.text = f"World clicks: {click_count}"


world.run()
