
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such 
that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total 
of A[P] + A[P+1] + ... + A[Q].

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice 
of A.

For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0

the function should return 5 because:

        (3, 4) is a slice of A that has sum 4,
        (2, 2) is a slice of A that has sum −6,
        (0, 1) is a slice of A that has sum 5,
        no other slice of A has sum greater than (0, 1).

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..1,000,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000];
        the result will be an integer within the range [−2,147,483,648..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/trainingZMFGQ3-CQA/ O(n)
"""

import time


def solution(A):
    """
    Simple max slice O(n) solution.
    Does not return indexes of max_slice[start:end]
    In this case negative numbers are in scope so the min(A) must be considered.
    """
    base = min(A)
    ending = 0
    max_slice = base
    for a in A:
        ending = max(base, ending + a, a)
        max_slice = max(max_slice, ending)
        # print(f'{i:02d} - A[i]: {a}, ending: {ending}, max_slice: {max_slice}')
    return max_slice


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (5,  ([3, 2, -6, 4, 0],)),
        (10, ([1, 2, 3, 4],)),
        (3,  ([3],)),
        (2,  ([-1, -2, 1, -4, 2, -5],)),
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