# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor
# https://codility.com/media/train/13-CaterpillarMethod.pdf

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R].
In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this
array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of
triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].

100% solution #https://app.codility.com/demo/results/training3G2UST-BS2/
O(N**2)
"""
import time
import random

def brute_force_validator(A):
    n = len(A)
    A.sort()
    result = 0
    for z in range(2, n):
        for y in range(1, z):
            for x in range(0, y):
                if A[x]+A[y] > A[z]:
                    result += 1
    return result

def ncr(r, n):
    if r == n:
        return 1
    elif r + 1 == n:
        return n
    elif r > n:
        return 0
    else:
        return r * ncr(r, n-1)

def solution(A):
    n = len(A)
    A.sort()
    result = 0

    for x in range(0, n-2): # A[z] always being the largest side of the triangle if A is 
        # print(f'Iteration {x}')
        y = x + 1
        z = x + 2
        # With A[z] being the largest side of the triangle, (A[x] + A[y]) > A[z] only needs proof
        while z<n:
            if A[x] + A[y] > A[z]:
                result += z - y
                z += 1
                # print(f'[{x}, {y}, {z-1}->{z}] - TRIANGLE  result is : {result}')
            
            # When the above condition fails every combination of x < y < z-1  is a triangle
            elif y < z - 1:
                y += 1
            else:
                y += 1; z += 1
    return result

if __name__ == '__main__':
    tests = (
        (4, ([10, 2, 5, 1, 8, 12],)),
        (3, ([3, 3, 5, 6],)),
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