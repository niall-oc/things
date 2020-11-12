
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

A non-empty array A consisting of N integers is given. A permutation is a sequence 
containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].


# 100% solution https://app.codility.com/demo/results/trainingQDTSP9-XV7/
"""

import time


def solution(A):
    n = len(A)
    res = n*(n+1)//2
    # Arithmetic guards against double numbers
    # Set check guards against anti sum cases
    return int((res == sum(A)) and (len(set(A)) == len(A)))


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (1, ([4, 1, 3, 2],)),
        (0, ([4, 1, 3],)),
        (1, ([1],)),
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