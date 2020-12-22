# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor
# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/

Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value
|A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.
Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal
abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range
[−1,000,000,000..1,000,000,000].

100% solution #https://app.codility.com/demo/results/trainingQC5CQ4-G2D/
O(N * log(N))
"""
import time

def brute_force_validator(A):
    n = len(A)
    A.sort()
    minimal = 2000000000
    for low in range(n):
        for high in range(n):
            minimal = min(abs(A[low] + A[high]), minimal)
    return minimal

def solution(A):
    n = len(A)
    A.sort()

    head = n-1
    tail = 0
    m = 2000000000
    while tail <= head:
        m = min(m, abs( A[tail] + A[head] ))
        if abs(A[tail]) > abs(A[head]) : # This will decide how to move the catepillar
            tail +=1
        else:
            head -= 1
    return m

if __name__ == '__main__':
    tests = (
        (1, ([1, 4, -3],)),
        (3, ([-8, 4, 5, -10, 3],)),
        (0, ([0],)),
        (4, ([2, 2],)),
        (6, ([8, 5, 3, 4, 6, 8],)),
        # (None, ([random.randint(1, 10000) for i in range(100)],)),
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