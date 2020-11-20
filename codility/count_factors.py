
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

A positive integer D is a factor of a positive integer N if there exists an integer 
M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition 
(24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, 
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/training9BYJJR-KVS/ O(sqrt(n))
"""

import time


def solution(N):
    """
    Work down from the square root to find lower factors that will yield higher factors
    """
    R = int(N**.5)
    result = 0
    
    for i in range(1, R+1):
        if not N%i:
            result = result + 2
    
    if R*R == N:
        result = result - 1
        
    return result


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (8,  (24,)),
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