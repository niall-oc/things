
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

# 100% solution https://app.codility.com/demo/results/trainingEHYUGC-S8D/
# 100% solution_other https://app.codility.com/demo/results/training99RBXN-YQ6/
"""

import time


def solution_other(A):
    """
    This solution preserves space complexity.
    """
    n = len(A)
    A.sort()
    
    # if there are no positive numbers then 1 is the smallest int missing
    # if there are only positive numbers and the array doesn't start at 1 then 1 is missing.
    if A[-1] < 1 or A[0] > 1:
        return 1

    # find first positive integer index
    current = 0
    while current < n:
        if A[current] > 0:
            break
        current += 1

    # If is not the first index then 1 is missing so return 1
    if A[current] > 1:
        return 1
    else:
        # Scanning forward if any next integer is more than 1 greater than the previous.
        for i in range(current+1, n):
            if A[i] - A[i-1] > 1:
                return A[i-1] + 1

    return A[-1] + 1


def solution(A):
    """
    Create an array 1 index greatar than A.
    EG. Given 20 numbers all positive in sequence 21 is missing.
    
    Scan A filling in the new array and report the missing positive integer.
    """
    n = len(A)

    MAX = n+1
    possible_answers = [0] * MAX

    
    for value in A:
        # if its positive and in range
        if 1 <= value <= MAX:
            # Insert a value at the correct index
            possible_answers[value-1] = value
    
    # Because this array only records positive integers from 1 onward
    # the first missing index encountered is the lowest int
    for index in range(MAX):
        if possible_answers[index] == 0:
            return index + 1

    return 1


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (5, ([1, 3, 6, 4, 1, 2],)),
        (4, ([1,2,3],)),
        (1, ([-1, -3],)),
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




