#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase
import square


class SquareTest(TestCase):

    def test_build_square_successfully(self):
        """
        Given
            1. x,y coord representing the top left of a square.
            2, Length of one edge.
        return
            ???
        """
        a_square = square.square((0,0), 2)
        expected_square = [(0,0), (0,2), (2,2), (2,0)]
        self.assertEquals(expected_square, a_square)
