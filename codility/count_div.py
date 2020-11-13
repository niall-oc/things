
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers 
within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, 
because there are three numbers divisible by 2 within the range [6..11], 
namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

# 100% solution https://app.codility.com/demo/results/trainingJWW77X-8J8/
"""

import time

def solution(A, B, K):
    # if A, B, K are already valid inputs!
    return ((B // K) + 1) - ((A + K -1) // K)


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (3, (6, 11, 2,)),
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




