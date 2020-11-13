
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/6-sorting/distinct/

Write a function

    class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

# 100% solution https://app.codility.com/demo/results/trainingDXWWYJ-E88/
# 100% solution_other https://app.codility.com/demo/results/trainingUZB7EV-D2A/
"""

import time


def solution_other(A):
    """
    Sort the array. Scan the array and only count everytime A[i] is greater than A[i-1]
    """
    n = len(A)

    if not n: # base case for 0
        return n

    A.sort()
    distinct_count = 1 # the first number is distinct!
    for i in range(1, n):
        if A[i] > A[i-1]:
            distinct_count += 1

    return distinct_count


def solution(A):
    return len(set(A))


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (3, ([2, 2, 2, 1, 1, 3],)),
        (1, ([1, 1],)),
        (2, ([-1, 1],)),
        (3, ([-1, -2, -3, -1, -2],)),
        (0, ([],)),
    )

    for expected, args in tests:
        # record performance of solution
        tic = time.perf_counter()
        res = solution_other(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')

        if args[0] is None:
            continue # This is just a speed test

        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')