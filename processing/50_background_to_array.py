from miniworlds import *

world = World()
arr = world.background.to_colors_array()
for i in range(0, len(arr),2 ):
    for j in range(len(arr[0])):
        arr[i][j][0] = 0
print(arr)
world.background.from_array(arr)
world.run()