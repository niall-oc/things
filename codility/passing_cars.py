
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

A non-empty array A consisting of N integers is given. The consecutive 
elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), 
where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is 
traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs 
of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 
1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following 
        values: 0, 1.

# 100% solution https://app.codility.com/demo/results/trainingZHN46P-DNM/
"""

import time


def solution(A):
    """
    For any car C travelling east the total remaining cars travelling west is equal
    to the number of passings occurring for  C.
    """
    n = len(A)
    if n<2:
        return 0

    total_west = sum(A)
    passing_count = 0
    for i in range(n):
        if not A[i]: # Travelling east
            passing_count += total_west
        else:
            total_west -= 1

    return passing_count if passing_count < 1000000001 else -1


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (5, ([0,1,0,1,1],)),
        (0, ([1, 1],)),
        (0, ([1],)),
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