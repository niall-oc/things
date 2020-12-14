# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. 
The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) 
prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These 
arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), 
where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

        (1, 26) is 10,
        (4, 10) is 4,
        (16, 20) is 0.

Write a function:

    def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M elements specifying the consecutive answers to 
all the queries.

For example, given an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..50,000];
        M is an integer within the range [1..30,000];
        each element of arrays P, Q is an integer within the range [1..N];
        P[i] ≤ Q[i].

# 100% solution https://app.codility.com/demo/results/trainingF5KA5F-PVP/ 
O(N * log(log(N)) + M) 
"""

import time

def get_sieve(n):
    # Use the sieve or eratosthenes to produce an array of primes
    factors = [0] * (n+1)
    i=2
    i2 = i*i
    while (i2 <= n):
        if not factors[i]:
            k = i2
            while k <= n:
                if not factors[k]:
                    factors[k] = i
                k += i
        i += 1
        i2 = i*i
    return factors

def is_semi_prime(n, factors):
    if factors[n]: # Check its not a prime
        for r in range(int(n**.5)+1, 1, -1):
            if not n%r:
                d = n//r
                return (not factors[d]) and (not factors[r])
    return False

def solution(N, P, Q):
    """
    1. produce a slope of increasing semi primes from 0 to N
    2. measure the increase from slope[Q[i]] to slope[P[i]]
    """
    factors = get_sieve(N)
    slope = [0] * (N+1)
    for i in range(1, N+1):
        slope[i] = slope[i-1] + is_semi_prime(i, factors) # Auto casting!! :-)
    # Optimus Prime!
    # print(list(enumerate(slope)))
    return [slope[Q[j]] - slope[P[j]-1] for j in range(len(P))]

if __name__ == '__main__':
    tests = (
        ( [10,4,0, 10, 11], (33, [1, 4, 16, 4, 1], [26, 10, 20, 28, 33]), ),
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