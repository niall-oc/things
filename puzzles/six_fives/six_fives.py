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

from math import factorial
from random import randint

SOLUTION = list(range(1, 101))

# Define operations
operators = "+-/*"

# Create lambdas for 5! and 5!!
f = lambda x: factorial(5)
ff = lambda x: factorial(factorial(5))

def create_base_gene(fives):
    """
    Create an equation using six 5's using the following heuristic.
    
    Randomly drop 5 between operators so that
    fives   -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
    becomes -> "5 + f(5) * ff(5) / 5 + 5 - ff(5)"
    """
    equation = ""
    while fives:
        equation = "{0} {1} ".format(equation, fives.pop())
        if fives: # If this is not the last 5
            equation = "{0} {1} ".format(equation, operators[randint(0,3)])
    return equation

def add_factorials(fives):
    """
    Randomly change 5 to be 5! or 5!! so that
    fives   -> ['5', '5', '5', '5', '5', '5']
    becomes -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
    """
    # 20% chance we will use ff(5) insteand of f(5)
    fact = lambda : 'ff(5)' if randint(0,10) > 8 else 'f(5)'
    # return the subbed fives
    return [fact() if randint(0,10) > 8 else five for five in fives]

def find_opening_parenthesis_pos(gene):
    """
    Randomly choose a position on the gene to insert opening parenthesis. 
    Suitable positions would be one of the following.
    
    - The begining.
    - Any space after an operator.
    
    :param str gene: A gene representing an equation.
    :return list: A sorted list of openings
    """
    openings = [0] # because 0 is a valid opening.
    for op in operators: # Look for the spaces after operators
        pos = gene.find(op, 1)
        while pos > 0: # while not past the end of the gene
            openings.append(pos+1)
            pos = gene.find(op, pos+1) # keep searching.
    return sorted(openings)

def find_closing_parenthesis_pos(gene):
    """
    Randomly choose a position on the gene to insert closing parenthesis. 
    Suitable positions would be one of the following.
    
    - The end.
    - Any space before an operator.
    
    :param str gene: A gene representing an equation.
    :return list: A sorted list of closings
    """
    ending = len(gene) -1
    closings = [ending] # because the end is a valid closing.
    for op in operators: # Look for the spaces after operators
        pos = gene.rfind(op, 0, ending)
        while pos > 0: # while not past the begining of the gene
            closings.append(pos-1)
            pos = gene.rfind(op, 0, pos-1) # keep searching.
    return sorted(closings)

def insert_parenthesis(gene):
    """
    Opening parenthesis can be inserted at the begining or after any operator.
    Closing parenthesis can be inserted at the end or after any 5, 5! or 5!!.
    Opening parenthesis must preceed any closing parenthesis.
    An insert involves placing both into a gene.
    """
    

def create_gene(use_adjoin_rule=False):
    """
    Create an equation using six 5's using the following heuristic.
    
    Randomly change 5 to be 5! or 5!! giving
        ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
    Randomly drop 5 between operators giving
        5 + f(5) * ff(5) / 5 + 5 - ff(5)
    Randomly insert Parenthesis pairs before or after fives giving
        (5 + 5) * 5 / 5 + 5 - 5
    
    :return str: equation to evaluate
    """
    fives = ['5', '5', '5', '5', '5', '5']
    # Randomly change some 5's to be 5! or 5!! 
    fives = add_factorials(fives)
    # we want five operators to join six 5's together
    equation = create_base_gene(fives)
    return equation

if __name__ == "__main__":
    # Randomly find solutions for numbers between 1 and 100
    results = dict()
    for i in range(10000):
        gene = create_gene()
        res = eval(gene)
        if isinstance(res, int) and res > 0 and res < 101:
            results[res] = (gene,) + results.setdefault(res, tuple())
    from pprint import pprint
    pprint(results)
    
