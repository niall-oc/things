
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N 
non-negative integers, specifying the radiuses of the discs, is given. The J-th disc 
is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs 
have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    class Solution { public int solution(int[] A); }

that, given an array A describing N discs as explained above, returns the number of 
(unordered) pairs of intersecting discs. The function should return −1 if the number 
of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/trainingTM9ZPN-ME9/
"""

import time


def solution(A):
    """
    Sort an array of disc lower bounds, and disc upper bounds..
    Iterate over the disc upper bounds and count all lower bounds.
        - NB: one of the lower bounds belongs to this disc.
    """
    N = len(A)
    # Sort the boundries of the discs
    indexes = range(0,N)
    upper_x = sorted([i+A[i] for i in indexes])
    lower_x = sorted([i-A[i] for i in indexes])
    print(f'upper_x: {upper_x}\nlower_x: {lower_x}')

    intersect_count = 0  # intersections counted
    l = 0
    for i in indexes:
        print(f'index: {i} upper_x[{i}]:{upper_x[i]}')
        while l < N and upper_x[i] >= lower_x[l]:
            print(f'upper_x[{i}]: {upper_x[i]}, lower_x[{l}]: {lower_x[l]}, N: {N}')
            l += 1

        # increment the difference between the circle beginings encountered - previous circles
        # also remove 1 because one of the beginngs encountered belongs to this disc
        intersect_count += l - i - 1
        print(f'intersect_count: {intersect_count} = l:{l} - i:{i} - 1')
        if intersect_count> 10000000:
            return -1
    return intersect_count


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (11, ([1, 5, 2, 1, 4, 0],)),
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