# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

An array A consisting of N different integers is given. The array contains integers 
in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

# 100% solution https://app.codility.com/demo/results/trainingX8QHZM-3QN/
"""

import time

def solution(A):
    """
    Euler states the sum of all integers is n(n+1)/2
    Knowing what sum is expected verses given allows us to determining 
    the missing integer.
    """
    given = sum(A)
    n = len(A) + 1 # n is the length the array should be with no number missing!
    expected = int((n*(n+1))//2)
    return expected - given


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (5, ([1, 2, 3, 4, 6, 7, 8, 9, 10],)),
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