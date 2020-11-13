
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/6-sorting/triangle/

An array A consisting of N integers is given. A triplet (P, Q, R) is 
triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns 1 if there 
exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range 
        [−2,147,483,648..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/trainingPE5D92-ETN/
"""

import time


def solution(A):
    """
    The largest side of a triangle must always be less than the sum of the other 2.
    Therefore in a sorted array A[i] < A[i-1] + A[i-2] singnals a triangle.
    """
    A.sort()
    N = len(A)
    i = 2
    if N > i: # Bunk out if there are not enough sides in the array.
        while i < N:
            if A[i-2] + A[i-1] > A[i]:
                return 1
            i+=1
    return 0


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (1, ([3, 4, 4],)),
        (0, ([3, 4, 8],)),
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