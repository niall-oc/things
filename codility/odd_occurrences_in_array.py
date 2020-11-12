# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/


A non-empty array A consisting of N integers is given. The array contains an odd 
number of elements, and each element of the array can be paired with another 
element that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, 
returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.


# 100% solution https://app.codility.com/demo/results/trainingCB48ED-3XU/
"""

import time

def solution(A):
    """
    Bitwise or between 2 numbers where N==N produces a 0.
    Therefore even pairing of numbers will produce zero.
    The remainder of the bitwise or operation will be equal to the one odd occurance 
    in the array.
    """
    result=0
    for item in A:
        result ^= item
    return result

if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (7, ([1,1,2,2,7],)),
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




