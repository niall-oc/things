# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor
# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/

An integer M and a non-empty array A consisting of N non-negative integers are
given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array
A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct
slice is a slice consisting of only unique numbers. That is, no individual
number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2),
(2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers,
returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function
should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].

100% solution https://app.codility.com/demo/results/training69FPP4-SFG/
"""
import time

def factorial(n):
    # check if the number is negative, positive or zero
    if n < 0:
        raise ValueError("Sorry, factorial does not exist for negative numbers")
    elif not n:
        return 1 # zero has a factorial of one
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial*i
        return factorial

def ncr(r, n):
    return factorial(n) // (factorial(r)*factorial(n-r))

def count_slices(n):
    total_slices = 0
    if n < 2:  
        total_slices += n
    else:
        total_slices += ncr(2, n) + n
    print(f'slice_length {n} produced {total_slices} slices')
    return total_slices

def solution(M, A):
    """
    The catepilar expands as it consumes new unique numbers. 
    As it grows the combination of slices contained within the range start to
    end is counted.
    When a duplicate is encountered the catepilar contracts until the set is
    unique.
    """
    n = len(A)

    if not n: # empty list
        return 0

    limit = 1000000000 # No more slices than this should be counted
    start = 0
    end = 0
    total_slices = 0
    duplicate = [0] * (M+1) # use an array to efficently mark numbers encountered

    while end < n and start < n: # don't overrun indexes

        while end < n and not duplicate[A[end]]: # expand when no duplicates found
            # print(f'A[{start}:{end}] -> {A[start:end+1]}')
            total_slices += end-start+1 # By factoring in the 1 this happens to be nCr(2, end-start)!
            duplicate[A[end]] = 1
            end += 1
            if total_slices > limit:
                return limit
        else:
            while end < n and start< n and A[start] != A[end]: # Move forward until start matches end
                duplicate[A[start]] = 0
                start += 1
            # Now move past the duplicate. This handles cases like [1, 1, 1] by counting [1], [1] and [1] as slices.
            duplicate[A[start]] = 0
            start += 1

    return total_slices


if __name__ == '__main__':
    tests = (
        (9, (6, [3, 4, 5, 5, 2],)),
        (5, (2, [1, 1, 1, 1, 1],)),
        (33, (10, [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9],)),
        (39, (10, [1, 2, 3, 4, 5, 6, 2, 8, 6, 7],)),
        (0, (1, [],)),
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        
        if expected is None:
            print(f'SPEED-TEST {len(args[0])} args finished in {toc - tic:0.8f} seconds')
            continue # This is just a speed test
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')