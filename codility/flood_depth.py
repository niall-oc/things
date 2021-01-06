# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/flood_depth/

You are helping a geologist friend investigate an area with mountain lakes.
A recent heavy rainfall has flooded these lakes and their water levels have
reached the highest possible point. Your friend is interested to know the
maximum depth in the deepest part of these lakes.

We simplify the problem in 2-D dimensions. The whole landscape can be divided
into small blocks and described by an array A of length N. Each element of A is
the altitude of the rock floor of a block (i.e. the height of this block when
there is no water at all). After the rainfall, all the low-lying areas (i.e.
blocks that have higher blocks on both sides) are holding as much water as
possible. You would like to know the maximum depth of water after this entire
area is flooded. You can assume that the altitude outside this area is zero and
the outside area can accommodate infinite amount of water.

For example, consider array A such that:

    A[0] = 1
    A[1] = 3
    A[2] = 2
    A[3] = 1
    A[4] = 2
    A[5] = 1
    A[6] = 5
    A[7] = 3
    A[8] = 3
    A[9] = 4
    A[10] = 2
The following picture illustrates the landscape after it has flooded:



The gray area is the rock floor described by the array A above and the blue area
with dashed lines represents the water filling the low-lying areas with maximum
possible volume. Thus, blocks 3 and 5 have a water depth of 2 while blocks 2, 4,
7 and 8 have a water depth of 1. Therefore, the maximum water depth of this area
is 2.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum
depth of water.

Given array A shown above, the function should return 2, as explained above.

For the following array:

    A[0] = 5
    A[1] = 8
the function should return 0, because this landscape cannot hold any water.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..100,000,000].

100% solution https://app.codility.com/demo/results/training6XM2NW-AX8/
O(n)
"""

import time

def max_lough_depth(A):
    """
    Everytime we descend there is the possibility of a body of water.
        Record max descent.
    Every time we ascend there is the possibility of containing the water.
        Record the point the water levels at and exit the water.
    """
    n = len(A)
    
    max_depth = 0;
    this_depth = 0;
    start_idx = 0; STARTED = False;
    print(f'A:{A}')
    for i in range(1, n):
        print(f'A[i-1]: {A[i-1]}, A[i]: {A[i]}')
        if not STARTED and A[i-1] > A[i]: # begin descent
            start_idx = i-1
            STARTED = True
            this_depth = max(this_depth, A[start_idx]-A[i])
            print(f'STARTING, start_idx: {start_idx}, A[start_idx]: {A[start_idx]}')
        elif STARTED:
            if A[i] >= A[start_idx]: # Lough formed
                max_depth = max(max_depth, this_depth)
                this_depth = start_idx = 0
                print(f'LOUGH FORMED from A[{start_idx}]: {A[start_idx]} to',
                      f'A[i]: {A[i]} - this_depth: {this_depth}, max_depth: {max_depth}')
                STARTED = False
            else:
                this_depth = max(this_depth, A[start_idx]-A[i])
                print(f'recording from A[{start_idx}]: {A[start_idx]} ->',
                      f'A[{i}]: {A[i]} - this_depth: {this_depth}')
    return max_depth

def solution(A):
    # Examine A going forward and back and discover the max depth in either case.
    print('FORWARD')
    forward =  max_lough_depth(A)
    print('BACKWARD')
    backward = max_lough_depth(A[::-1])
    print(f'forward:{forward}, backward:{backward}')
    return max(forward, backward)

if __name__ == '__main__':
    tests = (
        #( expected, args )
        #(2, ([1, 3, 2, 1, 2, 1, 5, 3, 3, 4],)),
        #(19, ([100, 50, 1, 3, 2, 4, 3, 6, 20, 5, 5, 5, 10],)),
        (1, ([2, 1, 3],)),
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
            print(f'ERROR {args} produced {res} when {expected} was expected!\n')
        
    