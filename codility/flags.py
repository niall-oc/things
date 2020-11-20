# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/



A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

        two flags, you can set them on peaks 1 and 5;
        three flags, you can set them on peaks 1, 5 and 10;
        four flags, you can set only three flags, on peaks 1, 5 and 10.

You can therefore set a maximum of three flags in this case.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..400,000];
        each element of array A is an integer within the range [0..1,000,000,000].

# 100% solution https://app.codility.com/demo/results/trainingQ55VRN-CJG/ O(n)
"""

import time

def solution(A):
    n = len(A)
    peaks = [i for i in range(1, n-1) if A[i] > A[i-1] and A[i] > A[i+1]]
    
    num_peaks = len(peaks)
    if num_peaks < 3:
        return num_peaks # with less than 3 peaks all flags can be placed
    
    max_flags  = int((peaks[-1]-peaks[0])**.5) # Cover the case of packed flags by adding 2
    
    # limit to trying optimal attempts, don't waste cycles trying 3,4,... etc if the most will be likely 300 flags
    flag_attempts = range(max_flags+1, 0, -1)
    # print(n, max_flags, num_peaks)
    most_flags = 0
    for attempt in flag_attempts: # we are limited from 3 to max flags or num peaks
        # print(attempt)
        flag_count = 1 # place flag at first peak
        next_flag = peaks[0] + attempt # reset the position of the next_flag for this attempt
        for p in peaks:
            # print(next_flag, p)
            if next_flag <= p: # it is possible to set a flag
                flag_count += 1
                next_flag = p + attempt # the next flag can go here
            if flag_count >= attempt: # when you run out of flags
                break

        if flag_count >= most_flags:
            most_flags = flag_count
        else:
            return most_flags # Stop when the solution starts to deteriorate!
    return most_flags

if __name__ == '__main__':
    tests = (
        (1, ([0,0,1,0,0],)),
        (4, ([0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0],)),
        (9, ([0]+[1,0]*36+[0]*30+[1,0],)),
        (632, ([0]+[1,0]*200000+[0],)),
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