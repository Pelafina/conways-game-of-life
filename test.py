import unittest
from grid import Grid
from cells import Cell

class CellTest(unittest.TestCase):
    def test_cell_creation(self):
        expected_cell = "alive False, neighbours 0" 
        test_cell = Cell()
        self.assertEqual(expected_cell, test_cell)

    def test_cell_comparison(self):
        dead_cell = Cell()
        alive_cell = Cell(True)
        self.assertEqual(dead_cell, dead_cell)
        self.assertEqual(alive_cell, alive_cell)
        self.assertNotEqual(dead_cell, alive_cell)
        self.assertNotEqual(dead_cell, 14)
        self.assertNotEqual(alive_cell, 53)
        self.assertNotEqual(dead_cell, f"dead_cell")

        cell_1_neighbour = Cell()
        cell_1_neighbour.neighbours = 1
        cell_1_neighbour_comparison = Cell()
        cell_1_neighbour_comparison.neighbours = 1
        self.assertEqual(cell_1_neighbour, cell_1_neighbour_comparison)

        cell_2_neighbour = Cell()
        cell_2_neighbour.neighbours = 2
        cell_2_neighbour_comparison = Cell()
        cell_2_neighbour_comparison.neighbours = 2
        self.assertEqual(cell_2_neighbour, cell_2_neighbour_comparison)

        self.assertNotEqual(cell_1_neighbour, cell_2_neighbour)
        self.assertNotEqual(cell_1_neighbour, dead_cell)

class GridTest(unittest.TestCase):
    def test_grid_creation(self):
        expected_grid_2x2 = [[Cell(), Cell()], [Cell(), Cell()]]
        test_grid_2x2 = Grid(2, 2)
        self.assertEqual(expected_grid_2x2, test_grid_2x2)

        expected_grid_3x3 = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]
        test_grid_3x3 = Grid(3, 3)
        self.assertEqual(expected_grid_3x3, test_grid_3x3)
        self.assertNotEqual(test_grid_2x2, test_grid_3x3)

    def test_add_delete_cells(self):
        grid1 = Grid(2,2)
        grid2 = Grid(2,2)

        grid1.add_cell((0,0))
        self.assertNotEqual(grid1, grid2)

        grid1.delete_cell((0,0))
        self.assertEqual(grid1, grid2)

    def test_check_neighbours(self):
        grid1 = Grid(2,2)
        grid2 = Grid(2,2)

        grid1.add_cell((0,0))
        self.assertNotEqual(grid1, grid2)
        grid1.check_neighbour_cells()
        #cell 0,0 should die, grid 1 and 2 should be equal
        self.assertEqual(grid1, grid2)

        grid1.add_cell((0,0))
        grid1.add_cell((0,1))
        grid1.add_cell((1,0))
        #cell 1,1 should turn alive
        grid1.check_neighbour_cells()
        grid1_comparison = Grid(2,2)
        grid1_comparison.add_cell((0,0))
        grid1_comparison.add_cell((0,1))
        grid1_comparison.add_cell((1,0))
        grid1_comparison.add_cell((1,1))
        self.assertEqual(grid1, grid1_comparison)
        # grid2.add_cell((1,0))






