# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog

The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially
located at one bank of the river (position −1) and wants to get to the other
bank (position N). The frog can jump over any distance F(K), where F(K) is the
K-th Fibonacci number. Luckily, there are many leaves on the river, and the
frog can jump between the leaves, but only in the direction of the bank at
position N.

The leaves on the river are represented in an array A consisting of N integers.
Consecutive elements of array A represent consecutive positions from 0 to N − 1
on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to
the other side of the river (from position −1 to position N). The frog can jump
between positions −1 and N (the banks of the river) and every position
containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of
jumps by which the frog can get to the other side of the river. If the frog
cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following
values: 0, 1.

# 100% solution https://app.codility.com/demo/results/training6C7RAP-RVJ/
O(N * log(N))
"""

import time

def gen_fib(n):
    fn = [0,1]
    i = 2
    s = 2
    while s < n:
        s = fn[i-2] + fn[i-1]
        fn.append(s)
        i+=1
    return fn

def new_paths(A, n, last_pos, fn):
    """
    Given an array A of len n.
    From index last_pos which numbers in fn jump to a leaf?
    returns list: set of indexes with leaves.
    """
    paths = []
    for f in fn:
        new_pos = last_pos + f
        if new_pos == n or (new_pos < n and A[new_pos]):
            paths.append(new_pos)
    return paths


def solution(A):
    n = len(A)
    if n < 3:
        return 1

    # A.append(1) # mark final jump
    fn = sorted(gen_fib(100000)[2:]) # Fib numbers with 0, 1, 1, 2..  clipped to just 1, 2..
    # print(fn)
    paths = set([-1]) # locate all the leaves that are one fib jump from the start position.

    jump = 1
    while True:
        # Considering each of the previous jump positions - How many leaves from there are one fib jump away
        paths =  set([idx for pos in paths for idx in new_paths(A, n, pos, fn)])

        # no new jumps means game over!
        if not paths:
            break

        # If there was a result in the new jumps record that
        if n in paths:
            return jump
            
        jump += 1

    return -1

if __name__ == '__main__':
    tests = (
        (3, ([0,0,0,1,1,0,1,0,0,0,0],)),
        (1, ([],)),
        (1, ([1],)),
        (1, ([0],)),
        (1, ([1, 1],)),
        (2, ([1,1,1],)),
        (5, ([0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0],)),
        (3, ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],)),
        (3, ([0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0],)),
        (-1, ([0, 1, 0, 0, 0],)),
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