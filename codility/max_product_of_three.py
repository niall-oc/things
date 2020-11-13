
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

A non-empty array A consisting of N integers is given. The product of triplet 
(P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A, returns the value of the maximal product of any 
triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

# 100% solution https://app.codility.com/demo/results/trainingYWFDB4-NM9/
"""

import time


def solution(A):
    """
    By sorting the array the largest numbers are either at A[1, 2, 3] or A[n-2, n-1, n]

    First:
    The largest negative numbers at index [0, 1] will multiply to a positive number.
    This should be then multiplied by the largest positive number to give X.

    Second:
    The largest positive numbers should all be multiplied by each other to give Y

    Finally:
    return the max(X, Y)
    """
    A.sort()
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (12, ([2, 2, 2, 1, 1, 3],)),
        (1, ([1, 1, 1],)),
        (-2, ([-1, 1, 2],)),
        (-24, ([-7, -8, -5, -4, -3, -2],)),
        (392, ([-7, -8, 5, 4, 6, 7],)),
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