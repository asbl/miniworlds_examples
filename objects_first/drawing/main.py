from miniworlds import World, Actor, Line

draw_color = (0,0,0)
line_started = False

world = World(600, 400)
color_red = Actor((0,360), origin = "topleft")
color_red.color = (255,0,0)

color_blue = Actor((40,360), origin = "topleft")
color_blue.color = (0,0,255)

color_green = Actor((80,360), origin = "topleft")
color_green.color = (0,255,0)

start_mouse_pos = None

@world.register
def on_mouse_left_up(self, end_pos):   
    global start_mouse_pos 
    if (start_mouse_pos):
        l = Line(start_mouse_pos, end_pos)
        l.stroke_color = draw_color
        l.static = True
    start_mouse_pos = None

@world.register
def on_mouse_left_down(self, pos):   
    global start_mouse_pos
    start_mouse_pos = pos

@color_red.register
def on_clicked(self, mouse_pos):
    global draw_color
    draw_color = color_red.color
    
@color_blue.register
def on_clicked(self, mouse_pos):
    global draw_color
    draw_color = color_blue.color
    
@color_green.register
def on_clicked(self, mouse_pos):
    global draw_color
    draw_color = color_green.color
    
world.run()