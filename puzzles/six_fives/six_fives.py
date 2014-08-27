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
from itertools import combinations

SOLUTION = list(range(1, 101))

# Define operations
operators = "+-/*"

# Create lambdas for 5! and 5!!
f = lambda x: factorial(5)
ff = lambda x: factorial(factorial(5))

def add_operators(fives):
    """
    Create an equation using six 5's using the following heuristic.
    
    Randomly drop operators between fives so that
    fives   -> ['5', 'f(5)', 'ff(5)', '5', '5', 'ff5()']
    becomes -> "5 + f(5) * ff(5) / 5 + 5 - ff(5)"
    
    :param list fives: The list of 5's
    :return str: fives with operators inserted
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
    
    :param list fives: The list of 5's
    :return list: fives with factorials inserted
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
    
    :param list fives: The list of 5's
    :return list: fives with parenthesis inserted
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

def create_gene():
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
    equation = add_operators(fives)
    return equation

def find_crossover_points(gene):
    """
    Find the crossover points in a gene.  This is defined as;
    
    - Any operater that is not inside parenthesis.
    
    :param str gene: an equation
    :return list: the possible crossover points
    """
    split_gene = gene.split()
    co_points = []
    in_parenthesis = 0
    for index in range(len(split_gene)):
        part = split_gene[index]
        if part in '+-/*' and not in_parenthesis:
            co_points.append(index)
        else:
            for char in part:
                if char == '(':
                    in_parenthesis += 1
                elif char == ')':
                    in_parenthesis -= 1
    return co_points

def crossover_genes(genes):
    """
    Using all the pair combinations of the genes. See if mating is possible.
    Append the new genes to the next generation
    """
    next_generation = []
    # For all the pairs than can be mated
    for combination in combinations(genes, 2):
        mam, dad = combination
        # Find the crossover points
        mam_options = find_crossover_points(mam)
        dad_options = find_crossover_points(dad)
        # Find the intersecting crossover points if any
        crossovers = set(mam_options).intersection(set(dad_options))
        # For any mate points
        for crossover in crossovers:
            mam_split = mam.split()
            dad_split = dad.split()
            # Grab the two crossover possibilities
            juniorM = ' '.join(mam_split[:crossover] + dad_split[crossover:])
            juniorD = ' '.join(dad_split[:crossover] + mam_split[crossover:])
            # Append to the next generation
            next_generation.append(juniorM)
            next_generation.append(juniorD)
    return next_generation


if __name__ == "__main__":
    # Randomly find solutions for numbers between 1 and 100
    results = dict()
    target = 100
    historical_genes = set()
    genes = [create_gene() for i in range(100)] # 100 genes per generation
    generation = 0
    while 0 not in results: # for 100 generations
        generation +=1
        results = dict()
        historical_genes.update(genes) # Record the genes used
        # Evaluate every gene
        for gene in genes:
            try:
                res = eval(gene)
                difference = abs(target-res)
                if difference < 100: # impose some fitness
                    results[difference] = (gene,) + results.setdefault(difference, tuple())
            except ZeroDivisionError:
                res = None
            # save the difference as the key
            
        if 0 in results: # stop if we found it
            print results.get(0)
            break
        else:
            # Need a new generation. start with the fittest
            best_genes = [g for key in sorted(results.keys())[:5] for g in results[key]]
            # Breed new genes but only take ones that haven't already been evaluated
            new_genes = set(crossover_genes(best_genes)).difference(historical_genes)
            genes = best_genes + list(new_genes)
            print "generation {0}".format(generation)
    from pprint import pprint
    pprint(results[min(results.keys())])
    print 'Search over, nearest is ', min(results.keys())
    
