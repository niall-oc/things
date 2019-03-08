"""
### FILL IN THE GRID PUZZLE

Objective: Arange the numbers 1 through 8 in the grid below.

        +---+---+
        |   |   |
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
        |   |   |
        +---+---+

RULES:
    No consecutive numbers may appear next to each other either vertically, horizontally or diagonally.
    Each number may only be used once.
"""

import unittest
import grid8


class Grid8Test(unittest.TestCase):
    def test_assign_to_grid(self):
        """
        Can we assign a number to a valid square on the grid
        """
        state = dict(grid8.GRID) # create a new grid
        grid_square = (1, 2,)
        new_state = grid8.assign_to_grid(grid_square, 1, state)
        # Assert the state changed after the assignemnt
        self.assertNotEqual(new_state, state)
        # Assert 1 is on the board
        self.assertIn(1, new_state.values())
        # Assert 1 is in the right position.
        self.assertEqual(new_state[grid_square], 1)

    def test_assign_to_filled_space(self):
        """
        Once a grid square has a value it cannot acccept any more values.
        raise ValueError
        """
        state = dict(grid8.GRID) # create a new grid
        grid_square = (1, 2,)
        new_state = grid8.assign_to_grid(grid_square, 1, state)
        # Assert 1 is in the right position.
        self.assertEqual(new_state[grid_square], 1)
        with self.assertRaises(ValueError):
            grid8.assign_to_grid(grid_square, 1, new_state)

    def test_invalid_grid(self):
        """
        The only valid grids are all members of GRID.keys()
               (1,2,) (1,3,)
        (2,1,) (2,2,) (2,3,) (2,4,)
               (3,2,) (3,3,)
        """
        state = dict(grid8.GRID) # create a new grid
        grid_square = (1, 9,)
        with self.assertRaises(KeyError):
            grid8.assign_to_grid(grid_square, 1, state)

    def test_assignment_is_valid(self):
        """
        RULES:
            - No consecutive numbers may appear next to each other either vertically,
              horizontally or diagonally.
            - Each number may only be used once
        """
        state = dict(grid8.GRID) # create a new grid
        grid_square = (1, 2,)
        is_valid = grid8.assignment_valid(grid_square, 1, state)
        # Assert the proposed move is valid
        self.assertTrue(is_valid)
        # Assign the move
        new_state = grid8.assign_to_grid(grid_square, 1, state)
        # Assert 1 is in the right position.
        self.assertEqual(new_state[grid_square], 1)
        ### All slots next to grid(1, 2,) should be invalid
        grid_square = (1, 3,)
        is_valid = grid8.assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 1,)
        is_valid = grid8.assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 2,)
        is_valid = grid8.assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 3,)
        is_valid = grid8.assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
