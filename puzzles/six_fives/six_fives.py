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
from copy import copy

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
        equation = "{0} {1} ".format(equation, fives.pop(0))
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

def add_parenthesis(fives):
    """
    Randomly insert Parenthesis pairs before or after fives so that
        5 + f(5) * ff(5) / 5 + 5 - ff(5)
    becomes
        (5 + f(5)) * ff(5) / (5 + 5) - ff(5)
    """
    new_fives = copy(fives)
    # Need to mark the end and set closing parenthesis position to 0
    end = len(new_fives)-1
    closep = 0
    # While a closing parenthesis has not been placed at the end.
    while closep < end:
        # Find a position to add an opening
        openp = randint(closep, end)
        # From the opening to the end find a position to add a closing.
        closep = randint(openp, end)
        # Add the opening and closing parenthesis
        new_fives[openp] = '({0}'.format(new_fives[openp])
        new_fives[closep] = '{0})'.format(new_fives[closep])
        closep += 1 # increment the closep to stop a double insert.
    return new_fives

def create_gene(use_adjoin_rule=False):
    """
    Create an equation using six 5's using the following heuristic.
    
    Randomly change 5 to be 5! or 5!! giving
        ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
    Randomly drop 5 between operators giving
        5 + f(5) * ff(5) / 5 + 5 - ff(5)
    Randomly insert Parenthesis pairs before or after fives giving
        (5 + f(5)) * ff(5) / (5 + 5) - ff(5)
    
    :return str: equation to evaluate
    """
    fives = ['5', '5', '5', '5', '5', '5']
    # Randomly change some 5's to be 5! or 5!! 
    fives = add_factorials(fives)
    # Insert parenthesis
    fives = add_parenthesis(fives)
    # we want five operators to join six 5's together
    equation = create_base_gene(fives)
    return equation

if __name__ == "__main__":
    # Randomly find solutions for numbers between 1 and 100
    results = dict()
    target = 64
    genes = [create_gene() for i in range(100)] # 100 genes per generation
    for i in range(100): # for 100 generations
        for gene in genes:
            try:
                res = eval(gene)
                difference = abs(target-res)
                if difference < 100:
                    results[difference] = (gene,) + results.setdefault(difference, tuple())
            except ZeroDivisionError:
                res = None
            # save the difference as the key
            
        if 0 in results: # stop if we found it
            print results.get(0)
            break
        else:
            #  Need to mutate and cross over here
            genes = [create_gene() for i in range(100)]
    from pprint import pprint
    pprint(results[min(results.keys())])
    print 'Search over, nearest is ', min(results.keys())
    
