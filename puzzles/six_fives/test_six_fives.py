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
    def test_add_operators(self):
        """
        Randomly drop operators between fives so that
        fives   -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
        becomes -> "5 + f(5) * ff(5) / 5 + 5 - ff(5)"
        
        Its random so a harness is not possible.
        """
        fives = ['5', '(f(5)', 'ff(5)', '5)', '5', 'ff(5)']
        fives = six_fives.add_operators(fives)
        self.assertIn('5', fives)
        checksum = [1 for c in fives if c == '('] + [-1 for c in fives if c == ')']
        self.assertEqual(sum(checksum), 0)
        fives  = [5 for f in fives if f == '5']
        self.assertEqual(len(fives), 6)
        
    
    def test_add_factorials(self):
        """
        Randomly change 5 to be 5! or 5!! so that
        fives   -> ['5', '5', '5', '5', '5', '5']
        becomes -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff(5)']
        
        Its random so a harness is not possible.
        """
        fives = six_fives.add_factorials(['5']*6)
        self.assertEqual(len(fives), 6)
        fives = ''.join(fives)
        checksum = [1 for c in fives if c == '('] + [-1 for c in fives if c == ')']
        self.assertEqual(sum(checksum), 0)
    
    def test_add_parenthesis(self):
        """
        Randomly insert parenthesis
        fives   -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff(5)']
        becomes -> ['5', '(f(5)', 'ff(5)', '5)', '5', 'ff(5)']
        
        Its random so a harness is not possible.
        """
        fives = six_fives.add_factorials(['5']*6)
        self.assertEqual(len(fives), 6)
        fives = ''.join(fives)
        checksum = [1 for c in fives if c == '('] + [-1 for c in fives if c == ')']
        self.assertEqual(sum(checksum), 0)
    
    def test_find_crossover_points(self):
        """
        Find the potential crossover points in an equation.
        Any operater that is not inside parenthesis is a potential crossover.
        """
        # There are 5 crossovers here.
        gene = "5 + f(5) * ff(5) / 5 + 5 - ff(5)"
        self.assertEqual(len(six_fives.find_crossover_points(gene)), 5)
        # There are 3 crossovers here.
        gene = "(5 + f(5)) * ff(5) / (5 + 5) - ff(5)"
        self.assertEqual(len(six_fives.find_crossover_points(gene)), 3)
        # There are 0 crossovers here.
        gene = "(5 + f(5) * ff(5) / 5 + 5 - ff(5))"
        self.assertEqual(len(six_fives.find_crossover_points(gene)), 0)
        
    def test_crossover_genes(self):
        """
        given the following
        ['5 + 5 * 5 + 5 * (5) - 5', '5 + 5 + 5 + (f(5) / 5 + 5)']
        the first three operators are crossovers.
        """
        genes = ['5 + 5 * 5 + 5 * (5) - 5', '5 + 5 + 5 + (f(5) / 5 + 5)']
        print six_fives.crossover_genes(genes)
        mam, dad = genes
        print six_fives.find_crossover_points(mam)
        print six_fives.find_crossover_points(dad)
        
        
