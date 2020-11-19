
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... 
+ A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of 
any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater 
than 17.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

# 100% solution https://app.codility.com/demo/results/trainingK57V65-35K/ O(n)
"""

import time


def solution(A):
    """
    Use a prefix scan technique.
    Walk array A and record all lower slices
    Walk array A and record all upper slices.
    Finally walk the prefix slice totals and find the max Double slice.
    """
    n = len(A)
    max_uppers = [0]*n
    max_lowers = [0]*n
    
    max_sum = 0
    for i in range(n-2, 0, -1):          
        max_sum = max(0, max_sum+A[i])
        max_lowers[i] = max_sum
    
    max_sum = 0
    for i in range(1, n-1):          
        max_sum = max(0, max_sum+A[i])
        max_uppers[i] = max_sum
    
    max_sum = 0
    for i in range(0, n-2):
        max_sum = max(max_sum, max_uppers[i] + max_lowers[i+2])

    return max_sum


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (17, ([3, 2, 6, -1, 4, 5, -1, 2],)),
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