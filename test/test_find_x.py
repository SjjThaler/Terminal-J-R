import unittest
from unittest.mock import patch
import game2  # Assuming your code is in a file named game2.py

class TestFindX(unittest.TestCase):
    
    @patch('game2.fetch_grid')
    def test_find_x_at_start(self, mock_fetch):
        mock_fetch.return_value = [
            ["x", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        self.assertEqual(game2.find_x(), (0, 0))

    @patch('game2.fetch_grid')
    def test_find_x_at_end(self, mock_fetch):
        mock_fetch.return_value = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "x"]
        ]
        self.assertEqual(game2.find_x(), (2, 9))

    @patch('game2.fetch_grid')
    def test_find_x_in_middle(self, mock_fetch):
        mock_fetch.return_value = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "x", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        self.assertEqual(game2.find_x(), (1, 5))

    @patch('game2.fetch_grid')
    def test_no_x_in_grid(self, mock_fetch):
        mock_fetch.return_value = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        self.assertIsNone(game2.find_x())

    @patch('game2.fetch_grid')
    def test_multiple_x_characters(self, mock_fetch):
        mock_fetch.return_value = [
            ["-", "-", "-", "x", "-", "-", "-", "x", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        # Expect the first "x" at (0, 3)
        self.assertEqual(game2.find_x(), (0, 3))

if __name__ == "__main__":
    unittest.main()
