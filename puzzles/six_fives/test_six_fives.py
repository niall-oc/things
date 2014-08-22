#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Construct the Integers 1-100 using Six 5s

Objective:

- Produce the integers 1-100 using only combinations of 6 fives and the
  mathematical operations: +, –, *, / and !.
- You may adjoin 5s together, so the number 55 is a possible combination of 2 5s.
- You may also use the operation !!, a double factorial.
  (Note: 5!! = 5*3*1 = 15.)
"""
import unittest
import six_fives

class TestSixFives(unittest.TestCase):
    def test_create_base_gene(self):
        """
        A gene *must* have six 5's.
        """
        gene = six_fives.create_base_gene(['5']*6)
        self.assertIn('5', gene)
        fives  = [5 for f in gene if f == '5']
        self.assertEqual(len(fives), 6)
    
    def test_add_factorials(self):
        """
        Randomly change 5 to be 5! or 5!! so that
        fives   -> ['5', '5', '5', '5', '5', '5']
        becomes -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
        
        Its random so a harness is not possible.
        """
        new_fives = six_fives.add_factorials(['5']*6)
        self.assertEqual(len(new_fives), 6)
