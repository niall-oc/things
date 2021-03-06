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
    ##     -->
    #              #

# Any dead cell with exactly three live neighbours becomes a live cell.

    #
    #      -->    ###
    #
"""
import random


def create_cells(start, end, percent):
    """
    Create cells in the box defined by start(x,y) to end(x,y).
    The density is determined by percent.
    """
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    number_of_cells = int((width*height) * (percent/100))
    new_cells = {
        (
            random.randint(min(start[0], end[0]), max(start[0], end[0])),
            random.randint(min(start[1], end[1]), max(start[1], end[1]))
        )
        for i in range(number_of_cells)
    }
    return new_cells


def find_surrounding(cell):
    """
    A surrounding is any space that is in within 1x or 1y of the current
    cell.

    >>> find_surrounding((0,0))
    set([(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)])

    :param tuple cell: The x,y position of the cell.
    :return set: The surrounding spaces
    """
    x, y = cell
    surrounding = {
        (xp, yp)
        for xp in (x-1, x, x+1)
        for yp in (y-1, y, y+1)
    }
    # The cell itself is not a surrounding space
    surrounding.remove(cell)
    return surrounding


def step(grid):
    """
    In the following order the rules for each step are executed.

    Any live cell with fewer than two live neighbours dies.
    Any live cell with two or three live neighbours remains alive.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.
    """
    # From every living cells perspective lets find the surrounding spaces.

    # This creates overlap.  The number of overlaps tells how many neighbours a
    # space has.  This is an interesting way to process our rules.

    # A dictionary is one way to count this information easily.  We can
    # count each time we insert a key/space to the dictionary.
    neighbour_count = {}
    # using a generator saves a bit of memory
    for space in (space for cell in grid for space in find_surrounding(cell)):
        neighbour_count[space] = neighbour_count.setdefault(space, 0) + 1

    # Preserve state between generations by creating a new grid.
    new_grid = set()

    for cell, count in neighbour_count.items():
        # Rule #2 letting living cells with 2 or 3 neighbours survive.
        if count in (2, 3) and cell in grid:
            new_grid.add(cell)
        # Rule #4 empty space with 3 living neighbours comes to life.
        if count == 3 and cell not in grid:
            new_grid.add(cell)
        # Rule 1 and 3 are implemented by default.
    return new_grid
