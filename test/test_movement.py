import unittest
import game2

class TestMovementFunction(unittest.TestCase):
    def setUp(self):
        """Set up a fresh map grid for each test."""
        global map_grid
        game2.map_grid = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "x"],
        ]

    def test_move_left(self):
        """Test moving left."""
        game2.movement("a")
        self.assertEqual(game2.find_x(), (10, 18))
    
    def test_move_up(self):
        """Test moving up."""
        game2.movement("w")
        self.assertEqual(game2.find_x(), (9, 19))

    def test_move_down_indexError(self):
        """Test moving down."""
        game2.movement("s")
        self.assertEqual(game2.find_x(), (0, 19))

    def test_move_right_indexError(self):
        """Test moving right."""
        game2.movement("d")
        self.assertEqual(game2.find_x(), (10, 0))

    def test_move_double_left(self):
        """Test moving left."""
        game2.movement("a")
        game2.movement("a")
        self.assertEqual(game2.find_x(), (10, 17))
    
    def test_move_double_up(self):
        """Test moving up."""
        game2.movement("w")
        game2.movement("w")
        self.assertEqual(game2.find_x(), (8, 19))

    def test_move_double_down_indexError(self):
        """Test moving down."""
        game2.movement("s")
        game2.movement("s")
        self.assertEqual(game2.find_x(), (1, 19))

    def test_move_double_right_indexError(self):
        """Test moving right."""
        game2.movement("d")
        game2.movement("d")
        self.assertEqual(game2.find_x(), (10, 1))

if __name__ == "__main__":
    unittest.main()
