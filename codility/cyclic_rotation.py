# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

An array A consisting of N integers is given. Rotation of the array means that 
each element is shifted right by one index, and the last element of the array 
is moved to the first place. 

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be 
shifted to the right K times.

Write a function:

    def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the 
array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given
    A = [0, 0, 0]
    K = 1

the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4

the function should return [1, 2, 3, 4]

Assume that:

        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].

In your solution, focus on correctness. The performance of your solution will 
not be the focus of the assessment.

# 100% solution https://app.codility.com/demo/results/training7KQRSA-A2R/
"""

import time

def solution(A, K):
    """
    Work out the position thet rotation would finish in.
    Return a new array of A[N-K-1:] + A[:N-K].
    Note in python A[N-K-1:] and A[-K:] will be equivilent.
    """
    N = len(A)
    if N:
        K = K%N # if K%N is 0 the array A is returned as is.
        if K:
            return A[-K:]+A[:N-K]
    return A

if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        ([0, 0, 0], ([0, 0, 0], 1,)),
        ([1,2,3,4], ([1,2,3,4], 4,)),
        ([9, 7, 6, 3, 8], ([3, 8, 9, 7, 6], 3,)),
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


