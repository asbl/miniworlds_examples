from miniworlds import *

world = World(600,400)
world.add_background("images/sunflower.jpg")
arr = world.background.to_colors_array()
constant = 1
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for color in arr[x][y]:
            color = color * constant
            if color > 255:
                color = 255
world.background.from_array(arr)
world.run()