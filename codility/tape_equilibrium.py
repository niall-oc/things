
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

A non-empty array A consisting of N integers is given. Array A represents numbers 
on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: 
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: 
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part 
and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A):

that, given a non-empty array A of N integers, returns the minimal difference that 
can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

# 100% solution https://app.codility.com/demo/results/trainingUAE8VE-26Y/
"""

import time

def solution(A):
    """
    Initially sum both sides of the split begining at position 0.
    With each increment you are removing from the sum of teh right to give to the left.
    """
    # Establish the minimum difference
    left = A[0]
    right = sum(A[1:])
    min_diff = abs(left - right)

    # iterate over the tape in array A
    for index in range(1, len(A)-1):
        # move a value from the right to the left
        left +=  A[index]
        right -= A[index]
        min_diff = min(min_diff, abs(left - right))

    return min_diff


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (1, ([3,1,2,4,3],)),
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



