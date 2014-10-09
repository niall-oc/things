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

def find_neighbours(cell, grid):
    """
    A neighbour is any living cell that is in within 1x or 1y of the current
    cell.  Consider the folowing
    
    (1, 1)  (2, 1)  (3, 1)
    (1,-1)  (2,-1)  (3,-1)  
    
    >>> find_neighbours((1,1))
    set([(1,-1), (2, 1), (2,-1)])
    
    :param tuple cell: The x,y position of the cell.
    :param set grid: The state of the universe.
    :return set: The neighbours of cell.
    """
    x, y = cell
    potential = set([(xp, yp) for xp in (x-1, x, x+1) for yp in (y-1, y, y+1)])
    # The cell itself is not a neighbour
    potential.remove(cell)
    return potential.intersection(grid)

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
    for cell in grid:
        neighbours = find_neighbours(cell, grid)
        if len(neighbours) in (2,3,):
            new_grid.add(cell)
        
    return new_grid
