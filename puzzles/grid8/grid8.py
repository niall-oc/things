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
