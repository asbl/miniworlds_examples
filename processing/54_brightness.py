from miniworlds import *

world = World(600,400)
world.add_background("images/sunflower.jpg")
arr = world.background.to_colors_array()
arr_new = arr.copy()
def brightness(r, g, b):
    return (int(r) + int(g) + int(b)) / 3

for x in range(len(arr)):
    for y in range(len(arr[0])):
        
        arr[x][y] = brightness(arr[x][y][0], arr[x][y][1], arr[x][y][2])
        
world.background.from_array(arr)
world.run()

