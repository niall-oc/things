
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# # https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

An array A consisting of N integers is given. It contains daily prices of a 
stock share for a period of N consecutive days. If a single share was bought 
on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such 
transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, 
the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because 
A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, 
a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum 
possible profit was 356. It would occur if a share was bought on day 1 and sold on 
day 5.

Write a function,

    def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock 
share for a period of N consecutive days, returns the maximum possible profit from 
one transaction during this period. The function should return 0 if it was impossible 
to gain any profit.

For example, given array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..400,000];
    each element of array A is an integer within the range [0..200,000].

# 100% solution https://app.codility.com/demo/results/trainingAXRGPF-WDB/ O(n)
"""

import time


def max_slice_prof(A, start, end):
    """
    Simple max slice O(n) solution.
    Does not return indexes of max_slice[start:end]
    """
    ending = 0
    max_slice = 0
    for i in range(start, end):
        ending = max(0, ending + A[i])
        max_slice = max(max_slice, ending)
        # print(f'{i:02d} - A[{i}]: {A[i]}, ending: {ending}, max_slice: {max_slice}')
    return max_slice


def solution(A):
    """
    Generate a new array with the price movements recorded for each day. Prefix scan!
    This new array can be max sliced. The max slice sum is the most profitable trade.
    """
    n = len(A)
    moves =[0]*n
    
    for i in range(1, n):
        moves[i] = A[i] - A[i-1]
    return max_slice_prof(moves, 0, n)


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (356, ([23171, 21011, 21123, 21366, 21013, 21367],)),
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