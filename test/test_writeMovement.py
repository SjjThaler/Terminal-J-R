import unittest
import game2  # Replace with the name of your module containing the implementation

class TestWriteMove(unittest.TestCase):
    def setUp(self):
        """Set up a fresh map grid for each test."""
        game2.map_grid = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "0", "/", "0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "n", "-", "-", "x", "-", "-", "-", "-", "-", "-", "-", "w"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ]

    def test_move_into_obstacle(self):
        """Test moving into an obstacle (e.g., "/")."""
        old_row, old_col = 6, 11  # Starting position of "x"
        new_row, new_col = 5, 8  # Obstacle at "/"
        game2.writeMove(new_row, new_col, old_row, old_col)
        self.assertEqual(game2.map_grid[6][11], "x")
        self.assertEqual(game2.map_grid[5][8], "/")


    def test_move_to_special_character(self):
        """Test moving into a cell with a special character like "n"."""
        old_row, old_col = 6, 11  # Starting position of "x"
        new_row, new_col = 6, 8  # Special character "n"
        game2.writeMove(new_row, new_col, old_row, old_col)
        self.assertEqual(game2.map_grid[old_row][old_col], "x")  # "x" remains in old position
        self.assertEqual(game2.map_grid[new_row][new_col], "n")  # Special character not overwritten

if __name__ == "__main__":
    unittest.main()
