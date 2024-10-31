map_grid = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "x", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

def fetch_grid(grid):
    return grid

def display_grid():
    grid = fetch_grid(map_grid)
    for row in grid:
        print("".join(row))

def movement(move):
    grid = fetch_grid(map_grid)
    grid 

def find_x():
    grid = fetch_grid(map_grid)
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "x":
                return row_index, col_index  # Return the coordinates of "x"
    return None  # Return None if "x" is not found

state = False

def main():
    while state == False:
        move = input()
        movement(move)