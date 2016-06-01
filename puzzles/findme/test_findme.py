#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import findme

class TestFindMe(unittest.TestCase):
    def setUp(self):
        findme.TOP_LEFT = (0,0)
        findme.BOTTOM_RIGHT = (3,3)

    def test_valid_initial_state(self):
        """
        Any entity on a defined grid must be within bounds.
        """
        
        out_of_bounds = (-1, 1)
        in_bounds = (1, 1)
        self.assertFalse(findme.validate_entity(out_of_bounds))
        self.assertTrue(findme.validate_entity(in_bounds))

    def test_valid_move(self):
        """
        Given a grid X by Y blocks insize a new move must respect the following.
        
        A move is either along the x axis or the y axis but not both.
        A move is only one block.
        A move cannot be outside the lower bound x,y or the upper bound x,y.
        """
        man=(1,0)
        new_move = findme.get_move(man)
        self.assertTrue(findme.validate_entity(new_move))
        self.assertNotEqual(new_move, man)
        move_x = bool(man[0] != new_move[0])
        move_y = bool(man[1] != new_move[1])
        impossible = move_x and move_y
        self.assertFalse(impossible)
