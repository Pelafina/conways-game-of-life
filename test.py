import unittest
from grid import Grid
from cells import Cell

class GridTest(unittest.TestCase):
    def test_grid_creation(self):
        expected_grid_2x2 = [[Cell(), Cell()], [Cell(), Cell()]]
        test_grid_2x2 = Grid(2, 2)
        self.assertEqual(expected_grid_2x2, test_grid_2x2)
        print("test 1")

        expected_grid_3x3 = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]
        test_grid_3x3 = Grid(3, 3)
        self.assertEqual(expected_grid_3x3, test_grid_3x3)
        print("test 2")




