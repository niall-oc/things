# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/


An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the 
perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals 
N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Write a function:

    def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle 
whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as 
explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..1,000,000,000].


# 100% solution https://app.codility.com/demo/results/training3ZQSXZ-XT9/ O(sqrt(N)) 
"""

import time


def solution(N):
    """
    """
    max_int_root = int(N**.5)
    
    # is it a square?
    if max_int_root**2 == N:
        return 4*max_int_root
    
    while N%max_int_root:
        max_int_root -= 1 # find the next highest commond divisor.
        
    B = N//max_int_root

    return 2 * (B+max_int_root)


if __name__ == '__main__':
    tests = (
        (22, (30,)),
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')