import pdb
import mapbank


class MapGrid:
    def __init__(self, initial_grid):
        self._grid = initial_grid

    def get_grid(self):
        return self._grid

    def set_grid(self, new_grid):
        self._grid = new_grid


# Instantiate the MapGrid object with the initial map grid
map_grid_instance = MapGrid([
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "0", "/", "0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "n", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "x"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
])


def display_grid():
    grid = map_grid_instance.get_grid()
    for row in grid:
        print("".join(row))


def movement(move):
    grid = map_grid_instance.get_grid()
    row_index, column_index = find_x()
    old_row, old_column = row_index, column_index

    if move == "w":
        row_index -= 1
    elif move == "s":
        row_index += 1
    elif move == "a":
        column_index -= 1
    elif move == "d":
        column_index += 1

    indexcheck = checkIndex(row_index, column_index, grid)
    if indexcheck == True:
        return
    else:
        write_move(row_index, column_index, old_row, old_column)


def write_move(row_index, column_index, old_row, old_column):
    grid = map_grid_instance.get_grid()
    if grid[row_index][column_index] != "-":
        grid[old_row][old_column] = "x"
    else:
        grid[old_row][old_column] = "-"
        grid[row_index][column_index] = "x"
    map_grid_instance.set_grid(grid)

def checkIndex(row_index, column_index, grid):
    try:
        try:
            _ = grid[row_index]
        except IndexError:
            map_grid_instance.set_grid(mapbank.map_grid2)
            return True

        try:
            _ = grid[row_index][column_index]
        except IndexError:
            map_grid_instance.set_grid(mapbank.map_grid2)
            return True

    except Exception as e:
        print(f"Unexpected error: {e}")

def find_x():
    grid = map_grid_instance.get_grid()
    for row_index, row_content in enumerate(grid):
        for col_index, cell in enumerate(row_content):
            if cell == "x":
                return row_index, col_index  # Return the coordinates of "x"
    return None  # Return None if "x" is not found


state = False


def main():
    while not state:
        move = input("Enter your move (w/a/s/d): ")
        movement(move)
        display_grid()


if __name__ == "__main__":
    main()
