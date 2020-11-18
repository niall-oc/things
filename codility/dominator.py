
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/8-leader/dominator/

An array A consisting of N integers is given. The dominator of array A is the 
value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element 
of array A in which the dominator of A occurs. The function should return −1 if 
array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range 
    [−2,147,483,648..2,147,483,647].

# 100% solution https://app.codility.com/demo/results/trainingEXJPJN-XTD/
# 100% solution_other https://app.codility.com/demo/results/trainingKWHPR8-C5B/
"""

import time


def solution_other(A):
    """
    In this solution we can sort the array in (index, value) pairs.
    This allows us to count the most common occurence, determine if it is the dominator
    and finally return a valid index
    """
    n = len(A)

    if n == 1: # the base case
        return 0
    elif not n:
        return -1

    B = sorted(enumerate(A), key=lambda x: x[1])
    # print(B)
    candidate_index = 0
    candidate_count = 0
    this_count = 1
    i = 1
    while i < n:
        # print(f'B[{i}][1]: {B[i][1]} == {B[i-1][1]} :B[{i-1}][1]')
        while i < n and B[i][1] == B[i-1][1]:
            this_count += 1
            i += 1
        # print(f'this_count" {this_count} > {candidate_count} :candidate_count')
        if this_count > candidate_count:
            candidate_count = this_count
            candidate_index = B[i-1][0]

        # print(f'candidate_count: {candidate_count}, candidate_index: {candidate_index}')
        this_count = 1
        i+=1

    return candidate_index if candidate_count > n // 2 else -1


def solution(A):
    """
    Push numbers that match the current stack head.
    Pop the head when it doesn't match the current number.
    Any numbers remaining on the stack occured more than n//2 times

    This solution does not lean on sorting the array
    """
    n = len(A)
    candidate = []
    index = []

    for i in range(n):
        if not candidate or A[i] == candidate[-1]:
            candidate.append(A[i])
            index.append(i)
        else:
            candidate.pop()
            index.pop()
        print(f'index: {index}, candidate: {candidate} - A[{i}] = {A[i]}')
    if candidate:
        count = sum([1 for i in A if i == candidate[0]])
        return index[0] if count > len(A) // 2 else -1
    return -1


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (8, ([1, 2, 3, 2, 4, 2, 5, 2, 2],)),
        (-1, ([2, 1, 1, 3, 4],)),
        (0, ([1],)),
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