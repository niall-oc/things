
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/8-leader/equi_leader/

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., 
A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

# 100% solution https://app.codility.com/demo/results/training9QB6P4-N8Q/  O(N)
# 100% solution_other https://app.codility.com/demo/results/trainingFBNRPA-VKA/  O(N)
"""

import time


def find_dominator(A):
    """
    """
    candidate = []
    index = []
    n = len(A)

    for i in range(n):
        if not candidate or A[i] == candidate[-1]:
            candidate.append(A[i])
            index.append(i)
        else:
            candidate.pop()
            index.pop()
    return candidate


def solution(A):
    """
    Find the dominator first.
    Then scan for ways to split the array A to determine how many equi leaders exist.

    Note sorting the array to find the dominator is not advisable here.
    This is an O(n) solution
    """
    n = len(A)
    candidate = find_dominator(A)
    
    if candidate: # There is a candidate
        # Determine where the candidate is positioned, and the candidate count.
        c_indexes = [int(i==candidate[0]) for i in A] # candidate indexes.
        candidate_total = sum(c_indexes)              # dominator count.
        
        if candidate_total > n // 2: # candidate is la dominator
            
            equi_leader_count = 0
            candidate_count = 0
            for i in range(n):
                if c_indexes[i]: # Everytime we pass a dominator we check to see if this position splits to produce an equileader.
                    candidate_count += 1
                equi_leader_count += (candidate_count > (i+1) // 2) and ((candidate_total - candidate_count) > (n-(i+1)) // 2)

            return equi_leader_count
    return 0


def solution_other(A):
    """
    Find the dominator first.
    Use a slope scan to find ways to split the dominator.

    This is an O(n) solution
    """
    n = len(A)
    candidate = find_dominator(A)

    if candidate: # we have a candidate
        # create a blank array
        scan = [0] * n
        # note the candidate
        c = candidate[0]
        # scan the 0 index for the candidate
        scan[0] = int(A[0] == c)
        # complete the scan from 1 - n
        for i in range(1, n):
            scan[i] = scan[i-1] + (A[i] == c)
        #print(scan)

        if scan[-1] > n//2: # the candidate is the dominator!
            equi_count = 0
            for i in range(n):
                equi_count += (scan[i] > (i+1) // 2) and ((scan[-1] - scan[i]) > (n-(i+1)) // 2)
            return equi_count
    return 0 


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (4, ([2, 3, 2, 4, 2, 5, 2, 2],)),
        (0, ([2, 1, 1, 3, 4],)),
        (3, ([4, 4, 2, 5, 3, 4, 4, 4],)),
        (0, ([0],)),
    )

    for expected, args in tests:
        # record performance of solution
        tic = time.perf_counter()
        res = solution_other(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')

        if args[0] is None:
            continue # This is just a speed test

        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')