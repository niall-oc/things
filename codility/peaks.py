# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/


An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the 
perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals 
N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Write a function:

    def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle 
whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as 
explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..1,000,000,000].


# 100% solution https://app.codility.com/demo/results/training5KP2PK-P4M/
O(N * log(log(N))) 
"""

import time

def get_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def solution(A):
    # determine N the lenght of the array
    N = len(A)
    if N<3:
        return 0 # no peaks in this case
    
    # scan the array to count the increasing slope of peaks.
    scan = [0]* N
    for i in range(1, N-1):
        if A[i] > max(A[i-1], A[i+1]):
            scan[i] = scan[i-1] + 1
        else:
            scan[i] = scan[i-1]
    scan[-1] = scan[-2] # tag last indexes
    
    if scan[0] == scan[-1]: # if no peaks occur then exit
        return 0
    
    # determine the divisors of len(A)
    h_div = int(N**.5)
    divisors = sorted({N} | {i for i in range(h_div, 1, -1) if not N%i} | {N//i for i in range(h_div, 1, -1) if not N%i}, reverse=True)

    # print(N, divisors, scan)
    result = 0
    for d in divisors:
        chunks = [(c[0], c[-1]) for c in get_chunks(scan, d)]
        # for all chunk if either a peak occurs  OR  the begining of the chunk is a peak!
        peaks = [(chunks[i][-1]-chunks[i][0]) or chunks[i][0] > chunks[max(i-1,0)][-1] for i in range(len(chunks))]
        if all(peaks):
            # print(chunks, peaks)
            result = max(result, len(chunks))
    return result

if __name__ == '__main__':
    tests = (
        (1, ([0,1,0,1,0],)),
        (2, ([0,1,0,1,0,0],)),
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')