# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

Two positive integers N and M are given. Integer N represents the number
of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only
a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1
chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the
chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following
chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat,
following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates
that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5,
as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].

# 100% solution https://app.codility.com/demo/results/trainingTQJ2KT-TEU/
O(log(N + M))
"""

import time

def division_sol(n, m):
    """
    The division solution has similar complexity but fails
    to pass the performance test for extreme large cases.
    Its worth noting that this solution cannot blow the recursion stack.
    """
    mod = n%m
    division = n//m
    start = end = m
    #print(n,m, mod, division, start, end)
    while mod:
        start = m - mod
        end = n - start
        mod = end%m
        division += (end//m) + 1
        #print(n,m, mod, division, start, end)
    return division

def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def solution(n, m):
    return n // gcd_division(n, m)

if __name__ == '__main__':
    tests = (
        ( 5, (10,4,)),
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