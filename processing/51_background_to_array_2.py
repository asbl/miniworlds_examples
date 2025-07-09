from miniworlds import *

world = World()
arr = world.background.to_colors_array()
print(arr)
for x in range(len(arr)):
    for y in range(len(arr[0])):
        arr[x][y][0] = ((x +1 ) / world.width) * 255
        arr[x][y][1] = ((y +1 ) /world.width) * 255
world.background.from_array(arr)
world.run()