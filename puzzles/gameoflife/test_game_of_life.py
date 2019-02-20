# -*- coding: utf-8 -*-
"""
Conways Game of Life

Rules

# Any live cell with fewer than two live neighbours dies.

    #      -->

# Any live cell with two or three live neighbours remains alive.

    ##     -->     ##
    #              #

# Any live cell with more than three live neighbours dies.

    #              #
   ###     -->    # #
    #              #

# Any dead cell with exactly three live neighbours becomes a live cell.

    #
    #      -->    ###
    #
"""
import unittest
import game_of_life


class GameOfLife(unittest.TestCase):
    """
    Conways Game of life infinite
    """
    def test_find_surrounding(self):
        """
        A surrounding is any space that is in within 1x or 1y of the current
        cell.

        >>> game_of_life.find_surrounding((0,0))
        set([(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)])
        """
        new_grid = game_of_life.find_surrounding((0, 0))
        expected = set([(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)])
        self.assertEqual(new_grid, expected)

    def test_rule_one(self):
        """
        # Any live cell with fewer than two live neighbours dies.

             #      -->

        """
        grid = set([(2, 2)])
        new_grid = game_of_life.step(grid)
        for cell in grid:
            self.assertNotIn(cell, new_grid)

    def test_rule_two(self):
        """
        # Any live cell with two or three live neighbours remains alive.

            ##     -->     ##
             #             ##
        """
        grid = set([(1, 0), (2, 0), (2, -1)])
        new_grid = game_of_life.step(grid)
        for cell in grid:
            self.assertIn(cell, new_grid)

    def test_rule_three(self):
        """
        # Any live cell with more than three live neighbours dies.

             #              #
            ###     -->    # #
             #              #
        """
        grid = set([(1, 0), (2, 0), (3, 0), (2, 1), (2, -1)])
        new_grid = game_of_life.step(grid)
        self.assertNotIn((2, 0), new_grid)

    def test_rule_four(self):
        """
        # Any dead cell with exactly three live neighbours becomes a live cell.

            #
            #      -->    ###
            #
        """
        grid = set([(1, 0), (2, 0), (3, 0)])
        new_grid = game_of_life.step(grid)
        self.assertNotIn((1, 0), new_grid)
        self.assertNotIn((3, 0), new_grid)
        self.assertIn((2, 0), new_grid)
        self.assertIn((2, 1), new_grid)
        self.assertIn((2, -1), new_grid)
