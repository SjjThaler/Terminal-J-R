
import game2
import random

map_grid2 = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "0", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "0", "/", "0","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "n", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "h", "a", "ll", "ooo", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["x", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "0", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "0", "/", "0","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "n", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]



map_walled = [
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w","w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "x","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "-", "-", "-", "-", "-", "-", "-", "-", "-","-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w","w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
]

def randomObject():
        new_map = map_walled
        row = random.randint(0, len(new_map) - 1)
        column = random.randint(0, len(new_map[0]) -1)
        map_walled[row][column] = "O"
        return new_map

a_new_map = randomObject()

        
