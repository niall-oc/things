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
    def test_find_neighbours(self):
        """
        A neighbour is any living cell that is in within 1x or 1y of the current
        cell.  Consider the folowing
        
        (1, 1)  (2, 1)  (3, 1)
        (1,-1)  (2,-1)  (3,-1)  
        
        >>> find_neighbours((1,1))
        set([(1,-1), (2, 1), (2,-1)])
        """
        grid = set([(1,1), (2,2), (3,3)])
        neighbours = game_of_life.find_neighbours((1,1), grid)
        self.assertIn((2,2), neighbours)
        self.assertNotIn((3,3), neighbours)
        neighbours = game_of_life.find_neighbours((2,2), grid)
        self.assertNotIn((2,2), neighbours)
        self.assertIn((3,3), neighbours)
        self.assertIn((1,1), neighbours)
        
    def test_rule_one(self):
        """
        # Any live cell with fewer than two live neighbours dies.
                        
             #      -->          
             
        """
        grid = set([(2,2)])
        new_grid = game_of_life.step(grid)
        self.assertNotIn((2,2), new_grid)
    
    def test_rule_two(self):
        """
        # Any live cell with two or three live neighbours remains alive.
                                
            ##     -->     ##   
            #              #    
        """
        grid = set([(1,0), (2,0), (2,-1)])
        new_grid = game_of_life.step(grid)
        self.assertEqual(grid, new_grid)
        
    def test_rule_three(self):
        """
        # Any live cell with more than three live neighbours dies.
                        
             #              #    
            ###     -->    # #   
             #              #    
        """
        grid = set([(1,0), (2,0), (3,0), (2,1), (2,-1)])
        new_grid = game_of_life.step(grid)
        self.assertNotIn((2,0), new_grid)
