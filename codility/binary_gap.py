# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

A binary gap within a positive integer N is any maximal sequence of consecutive 
zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of 
length 2. The number 529 has binary representation 1000010001 and contains two 
binary gaps: one of length 4 and one of length 3. The number 20 has binary 
representation 10100 and contains one binary gap of length 1. The number 15 has 
binary representation 1111 and has no binary gaps. The number 32 has binary 
representation 100000 and has no binary gaps.

Write a function:

    class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary 
representation 10000010001 and so its longest binary gap is of length 5. Given 
N = 32 the function should return 0, because N has binary representation '100000' 
and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].


# 100% solution https://app.codility.com/demo/results/trainingQ78427-3C2/
"""

import time

def solution_old(N):
    """
    Render N as a string and process the bits
    """
    count = binary_gap = 0
    for b in "{0:b}".format(N):
        if b == '1':
            binary_gap = max(count, binary_gap)
            count = 0
        else:
            count += 1
    return binary_gap

def solution(N):
    """
    Use bit shifting to process the bits
    """
    count = binary_gap = 0
    for i in range(64): # 64 bit machine. Just to be sure! :-)
        bit_on = N & (1 << i)
        if bit_on:
            binary_gap = max(count, binary_gap)
            count = 0
        else:
            count += 1
    return binary_gap
    

if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (5, (1041,)),
    )

    for expected, args in tests:
        # record performance of solution
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')

        if args[0] is None:
            continue # This is just a speed test

        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')

