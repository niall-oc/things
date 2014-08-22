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

from   copy import deepcopy
import unittest

# Operating on the premise that a gird is in reality a collection of x,y coordinates.
# A grid state could be
# {               (1,2,): 1,    (1,3,): None,
#   (2,1,): None, (2,2,): None, (2,3,): None, (2,4,): None,
#                 (3,2,): None, (3,3,): None }
#     +---+---+
#     | 1 |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
#     |   |   |
#     +---+---+
# At the begining of the game no number is assigned to any position on the grid.

GRID = {
    (1,2,): None,
    (1,3,): None,
    (2,1,): None,
    (2,2,): None,
    (2,3,): None,
    (2,4,): None,
    (3,2,): None,
    (3,3,): None
}

def find_neighbours(cell):
    """
    Given a cell with coords (x,y) the neighbours are:
        (x-1, y-1), ( x , y-1), (x+1, y-1),
        (x-1,  y ),             (x+1,  y ),
        (x-1, y+1), ( x , y+1), (x+1, y+1),
    The center space is (x,y) which is the cell itself and not a neighbour.
    """
    neighbours = set()
    x, y = cell
    for x_comp in (x-1, x, x+1):
        for y_comp in (y-1, y, y+1):
            neighbours.add((x_comp, y_comp))
    neighbours.remove(cell)
    return neighbours

def assignment_valid(grid_square, value, state):
    """
    Find all neighbouring grids on the board that have values.
    Ensure that the value is not within 1 of of the assignment value.

    value |  neighbours   | valid |
    ------+---------------+-------|
      1   | 3, 4, 2       | False | because 2 is next to 1
      1   | 3, 6, 8       | True  |
    """
    # neighbours should be there for one another!
    # neighbours are the set of grid squares surrounding the x, y coords given
    # that also intersect with the squares in state.keys()
    neighbours = set(state.keys()).intersection(find_neighbours(grid_square))
    # for any neighbour who is not None
    # if the abs(neighbour-value) is > 1 the move is valid
    # TIP: use a list comprehension to cycle through all neighbours who are not None
    #      recording the boolean equivilent of abs(neighbour-value) > 1.
    #      use the all() function to check all items in the lits are True
    is_valid = all(
        [
            bool(abs(state[neighbour]-value) > 1)
            for neighbour in neighbours
            if state[neighbour] is not None
        ]
    )
    return is_valid

def assign_to_grid(grid_square, value, state):
    """
    Assigns value to grid_square within a copy of state.

    :param tuple grid_square: An (x, y,) tuple representing a square on the board.
    :param int value: The value we want to assign.
    :param dict state: The state of the universe.
    :return dict: The updated state of the universe.
    """
    new_state = deepcopy(state)
    if new_state[grid_square] is None:
        new_state[grid_square] = value
    else:
        raise ValueError('{0} contains value {1}'.format(grid_square, value))
    return new_state

class Grid8Test(unittest.TestCase):
    def test_assign_to_grid(self):
        """
        Can we assign a number to a valid square on the grid
        """
        state = dict(GRID) # create a new grid
        grid_square = (1, 2,)
        new_state = assign_to_grid(grid_square, 1, state)
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
        state = dict(GRID) # create a new grid
        grid_square = (1, 2,)
        new_state = assign_to_grid(grid_square, 1, state)
        # Assert 1 is in the right position.
        self.assertEqual(new_state[grid_square], 1)
        with self.assertRaises(ValueError):
            assign_to_grid(grid_square, 1, new_state)

    def test_invalid_grid(self):
        """
        The only valid grids are all members of GRID.keys()
               (1,2,) (1,3,)
        (2,1,) (2,2,) (2,3,) (2,4,)
               (3,2,) (3,3,)
        """
        state = dict(GRID) # create a new grid
        grid_square = (1, 9,)
        with self.assertRaises(KeyError):
            assign_to_grid(grid_square, 1, state)

    def test_assignment_is_valid(self):
        """
        RULES:
            - No consecutive numbers may appear next to each other either vertically,
              horizontally or diagonally.
            - Each number may only be used once
        """
        state = dict(GRID) # create a new grid
        grid_square = (1, 2,)
        is_valid = assignment_valid(grid_square, 1, state)
        # Assert the proposed move is valid
        self.assertTrue(is_valid)
        # Assign the move
        new_state = assign_to_grid(grid_square, 1, state)
        # Assert 1 is in the right position.
        self.assertEqual(new_state[grid_square], 1)
        ### All slots next to grid(1, 2,) should be invalid
        grid_square = (1, 3,)
        is_valid = assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 1,)
        is_valid = assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 2,)
        is_valid = assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)
        grid_square = (2, 3,)
        is_valid = assignment_valid(grid_square, 2, new_state)
        # Assert the proposed move is valid
        self.assertFalse(is_valid)


def solve(state):
    """
    Recursive solution that uses a brute force approach to findindg the solution.

    2 essential facts are derived from the board state.
        - The number of empty spaces left.
        - The choice of numbers remaining.

    Solve for a given state
    The base case:
        If no there is no empty spaces the game is over so retrun the end state.
    The recursive case:
        While there are empty spaces, AND while there are choices remaining.
            If you can make a valid assignment,
                then assign the number to the board to create a new state.
                Solve for the new state. <------ Recursion, back to the top with a new step
            Else
                Try another number in this space.
                OR
                None of the numbers fit here so try them in another space.
    Everything failed

    :param dict state: the state of the board
    :return dict: the end state of the game.  None means no solution.
    """
    # uncomment the line below if you would like to see a trace.
    # print state

    # Derive the number of empty spaces left and the choices remaining to go on the board
    empty_spaces = [g for g, v in state.items() if v is None]
    numbers_used = [v for g, v in state.items() if v]
    numbers_left = [n for n in (1,2,3,4,5,6,7,8,) if n not in numbers_used]

    ### BASE CASE
    if not empty_spaces:
        return state

    ### RECURSIVE CASE
    while empty_spaces:
        # Treat the remaining options like a stack
        grid_square = empty_spaces.pop(0) # Grab the next space available
        while numbers_left:
            value = numbers_left.pop(0)   # Grab the next number available

            # If we can make an assignment
            if assignment_valid(grid_square, value, state):

                # Make a new state by assiging a number
                new_state = assign_to_grid(grid_square, value, state)
                ### RECURSION
                # Try to solve things from this state
                # Remember, if the base above is returned then this is where we will catch it.
                new_state = solve(new_state)

                if new_state: # return the solution
                    return new_state
                # If the state was none we will implicitly try the remaining numbers or spaces
                # in this branch of the solution tree.

    # No sweat, if this branch is exhausted return None.
    # This may be the last branch meaning the state we started in coudln't be solved.
    return None


if __name__ == "__main__":
    # create a new state
    state = deepcopy(GRID)

    # create a board for printing purposes
    board = """SOLUTION!! :-)
    +---+---+
    | {0} | {1} |
+---+---+---+---+
| {2} | {3} | {4} | {5} |
+---+---+---+---+
    | {6} | {7} |
    +---+---+\n"""

    # Cycle through all the possible starting points to see how many solutions there are.
    for start in (1,2,3,4,5,6,7,8,):
        # Assign a starting point.
        new_state = assign_to_grid((1, 2,), start, state)
        # try to solve from here
        solution = solve(new_state)

        if solution: # print a solution if we got one
            values = [solution[k] for k in sorted(solution.keys())]
            print board.format(*values)
