# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/

A prime is a positive integer X that has exactly two distinct divisors:
1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there
exists a positive integer K such that D * K = P. For example, 2 and
5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check
whether the sets of prime divisors of integers N and M are exactly
the same.

For example, given:

    N = 15 and M = 75, the prime divisors are the same: {3, 5};
    N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is
    not equal to {2, 3, 5};
    N = 9 and M = 5, the prime divisors aren't the same: {3} is not
    equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the
number of positions K for which the prime divisors of A[K] and B[K]
are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the
same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range
[1..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/trainingYZA3X2-JA4/
O(Z * log(max(A) + max(B))**2)
"""

import time

def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def prime_reduce(n, gcd):
    na = n // gcd
    ngcd = gcd_division(na, gcd)
    if na == 1:
        return True # success base case
    elif ngcd == 1:
        return False
    return prime_reduce(na, ngcd)

def solution(A, B):
    Z = len(A)
    result = 0
    for i in range(0, Z):
        a, b = A[i], B[i]
        if a == b:
            result += 1
        else:
            gcd = gcd_division(a, b)
            result += (prime_reduce(a, gcd) and prime_reduce(b, gcd))
    return result

if __name__ == '__main__':
    tests = (
        (1, ([15, 10, 9], [75, 30, 5]) ),
        (2, ([7, 17, 5, 3], [7, 11, 5, 2]) ),
        (2, ([3, 9, 20, 11], [9, 81, 5, 13]) ),
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