# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

There are N ropes numbered from 0 to N − 1, whose lengths are given in an array
A, lying on the floor in a line. For each I (0 ≤ I < N), the length of rope I on
the line is A[I].

We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied
together with a knot, and the length of the tied rope is the sum of lengths of
both ropes. The resulting new rope can then be tied again.

For a given integer K, the goal is to tie the ropes in such a way that the
number of ropes whose length is greater than or equal to K is maximal.

For example, consider K = 4 and array A such that:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 1
    A[5] = 1
    A[6] = 3
The ropes are shown in the figure below.



We can tie:

rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
After that, there will be three ropes whose lengths are greater than or
equal to K = 4. It is not possible to produce four such ropes.

Write a function:

def solution(K, A)

that, given an integer K and a non-empty array A of N integers, returns the
maximum number of ropes of length greater than or equal to K that can be created.

For example, given K = 4 and array A such that:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 1
    A[5] = 1
    A[6] = 3
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [1..1,000,000,000];
each element of array A is an integer within the range [1..1,000,000,000].

100% solution #https://app.codility.com/demo/results/trainingZZHSCF-A9R/
O(N)
"""
import time

def solution(K, A):
    rope_count = 0
    this_rope = 0
    
    for part in A: # bits of rope are processed in sequence!
        this_rope += part
        if this_rope >= K: # when this_rope is large enough start making a new rope
            rope_count += 1
            this_rope = 0
 
    return rope_count

if __name__ == '__main__':
    tests = (
        (3, (4, [1,2,3,4,1,1,3],)),
        (5, (5, [1,2,3,4,1,1,1,3,5,6],)),
        (1, (1, [1],)),
        (0, (2, [1],)),
        (5, (4, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3],)),
        (5, (5, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 3],)),
        (4, (5, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3],)),
        (3, (4, [1, 1, 1, 4, 1, 1, 1, 2, 1, 1, 1, 2, 1])),
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