# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/


You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements 
of the array that are not the divisors of A[i]. We say that these elements are 
non-divisors.

For example, consider integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

For the following elements:

        A[0] = 3, the non-divisors are: 2, 6,
        A[1] = 1, the non-divisors are: 3, 2, 3, 6,
        A[2] = 2, the non-divisors are: 3, 3, 6,
        A[3] = 3, the non-divisors are: 2, 6,
        A[4] = 6, there aren't any non-divisors.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers 
epresenting the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..50,000];
        each element of array A is an integer within the range [1..2 * N].

# 100% solution https://app.codility.com/demo/results/trainingH93PHF-566/ O(n*log(n))
"""

import time

def get_divisors(n):
    froot = int(n**.5)
    divs = set()
    # reverse through possible divisors which are lower than root(n)
    while froot > 0:
        if not n%froot:
            divs.add(froot)
            divs.add(n//froot) # Catch the higher diviser on the other side of froot
        froot-=1
    return divs

def solution(A):
    """
    1. scan the array and record the frequency of all integers.
    2. for each divisor find its frequency in the array.
    3. Non Divisors = N - The total occurence of all divisors
    """
    N = len(A)
    int_count = {}
    
    # O(N) scan to count number frequency
    for i in A:
        int_count[i] = int_count.get(i, 0) + 1
    
    # Create an array for every i's non-divisor count
    non_div_count = {}
    
    for i, _ in int_count.items(): # only calculate numbers once
        divs = get_divisors(i)
        # non-divisors = N -  divisors :-)
        non_div_count[i] = N - sum([int_count.get(d, 0) for d in divs])
        
    return [non_div_count[i] for i in A]

if __name__ == '__main__':
    tests = (
        ([2, 4, 3, 2, 0], ([3, 1, 2, 3, 6],)),
        ([0], ([2],)),
        #(None, (range(30000),)),
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