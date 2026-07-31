import unittest
from grid import Grid
from cells import Cell

class CellTest(unittest.TestCase):
    def test_cell_creation(self):
        expected_cell = "alive False, neighbours 0" 
        test_cell = Cell()
        self.assertEqual(expected_cell, test_cell)

class GridTest(unittest.TestCase):
    def test_grid_creation(self):
        expected_grid_2x2 = [[Cell(), Cell()], [Cell(), Cell()]]
        test_grid_2x2 = Grid(2, 2)
        self.assertEqual(f"{expected_grid_2x2}", test_grid_2x2)

        expected_grid_3x3 = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]
        test_grid_3x3 = Grid(3, 3)
        self.assertEqual(expected_grid_3x3, test_grid_3x3)




