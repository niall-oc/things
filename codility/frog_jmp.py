# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

A small frog wants to get to the other side of the road. The frog is currently 
located at position X and wants to get to a position greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its 
target.

Write a function:

    def solution(X, Y, D):

that, given three integers X, Y and D, returns the minimal number of jumps from 
position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.

# 100% solution https://app.codility.com/demo/results/trainingWK4W5Q-7EF/
"""

import time

def solution(X, Y, D):
    """
    Simply divide the jumps into the distance.
    Distance being y-X and ensuring a finaly jump over the line!
    """
    distance = (Y-X)
    hops = distance // D
    if distance%D: # landing even is not over the line!
        hops += 1
    return hops


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (3, (10, 85, 30,)),
    )

    for expected, args in tests:
        # record performance of solution
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')

        if args[0] is None:
            continue # This is just a speed test

        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')
