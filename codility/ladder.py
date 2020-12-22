# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/

You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1
to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the
ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return
the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array
consisting of L integers specifying the consecutive answers; position I should
contain the number of different ways of climbing the ladder with A[I] rungs
modulo 2B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].

100% solution # https://app.codility.com/demo/results/trainingFBCNGQ-X7B/
O(L)
"""

import time

def gen_fib(n):
    fn = [0] * n
    fn[1] = 1
    for i in range(2, n):
        fn[i] = fn[i-2] + fn[i-1]
    return fn

def solution(A, B):
    """
    The different arangements or combinations of adding 1 or 2 to get a number
    is also the fibonacci sequence!

    Consider the number of ways 5 can be created from using combinatinos 1 or 2.
    
    If you choose 2 first then:
        2 + (1+1+1) or 2 + (2+1) or 2 + (1+2)
    are all possible solutions.

    More formally the number 2 + the number of combinations for making 3 from
    the numbers 2 or 1!
    
    If you choose 1 first when trying to make 5 then:
        1 + (1+1+1+1) or 1 + (2+2) or 1 + (1+2+1) or 1 + (2+1+1) or 1 + (1+1+2)
    are all possible solutions.
    
    More formally the number 1 + the 5 combinations you can make 4 from!

    8 combinations = 3 combinations + 5 combinations!

    so f(n) = f(n-2) + f(n-1). . . !

    That's the fibonacci sequence! but with an offset.

    0 = choose nothing to make zero with is technically 1 way!

    1 = 1 there is only 1 solution to make 1
    2 = 2 +(0) or 1+(1) choose 2 first or 1 and the number of ways to make 1.

    0, 1, 2, 3, 4, 5,  6,  7,  8 etc.
    1, 1, 2, 3, 5, 8, 13, 21, 34 etc. 

    The answer is in fact:  The number of ways to climb a ladder ( in 1 or 2
    step combinations) is the same as fib(n-1) That implies you must shift the
    offset your fn series to get the correct number!
    """

    # A and B are equal length
    n = len(A)

    # any number in a can be between 0 and n
    fn_series = gen_fib(n+2)[1:] # Note. .  0, 1, and 2 are special, so shift the array and make it long enough for fn_series[A[i]] to succeed.

    # The result is a list of numbers representing fib(A[i]) % 2^B[i].for all i between 0 and n.

    # precompute B for speed on large arrays.

    pB = {i: (2**i) -1 for i in range(1, 31)}

    result = [fn_series[A[i]]&(pB[B[i]]) for i in range(n)]
    # https://stackoverflow.com/questions/6670715/mod-of-power-2-on-bitwise-operators/6670766#6670766
    # Best explains why bitwise & is faster than mod for this calculation.
    return result



if __name__ == '__main__':
    tests = (
        ([2, 3, 2, 1] , ([2, 3, 2, 4], [2, 2, 3, 2])),
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