#!/usr/bin/python
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
    surrounding = set([(xp, yp) for xp in (x-1, x, x+1) for yp in (y-1, y, y+1)])
    # The cell itself is not a surrounding space
    surrounding.remove(cell)
    return surrounding

def find_neighbours(cell, grid):
    """
    A neighbour is any living cell that is in within 1x or 1y of the current
    cell.  Consider the folowing
    
    (1,1)  (2,1)  (3,1)
    (1,0)  (2,0)  (3,0)  
    
    >>> find_neighbours((1,1))
    set([(1,0), (2,0), (2,1)])
    
    :param tuple cell: The x,y position of the cell.
    :param set grid: The state of the universe.
    :return set: The neighbours of cell.
    """
    potential = find_surrounding(cell)
    return potential.intersection(grid)

def find_spaces_around_cells(grid):
    """
    For every cell in the grid find the surrounding spaces.
    
    :param set grid: The state of the universe.
    :return set: The set of spaces surrounding cells.
    """
    spaces = set()
    for cell in grid:
        # Find all the cells around this one
        surrounding = find_surrounding(cell)
        # Determine which of the surrounding spaces have no cells
        # Add those spaces to the spaces set
        spaces = spaces.union(surrounding.difference(grid))
    return spaces

def step(grid):
    """
    In the following order the rules for each step are executed.
    
    Any live cell with fewer than two live neighbours dies.
    Any live cell with two or three live neighbours remains alive.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.
    """
    # rule 1.
    new_grid = set()
    # For each cell in the grid only allow those with 2 or 3 neoghbours to live.
    for cell in grid:
        neighbours = find_neighbours(cell, grid)
        if len(neighbours) in (2,3,):
            new_grid.add(cell)
    
    # For each space around a cell only allow those with 3 neighbours to live.
    for space in find_spaces_around_cells(grid):
        neighbours = find_neighbours(space, grid)
        if len(neighbours) == 3:
            new_grid.add(space)
    
    return new_grid
