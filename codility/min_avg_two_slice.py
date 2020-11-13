
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), 
such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice 
contains at least two elements). The average of a slice (P, Q) is the sum of 
A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, 
the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting 
position of the slice with the minimal average. If there is more than one slice 
with a minimal average, you should return the smallest starting position of such 
a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

# 100% solution https://app.codility.com/demo/results/trainingNQVFHH-JVW/
# 100% solution_other https://app.codility.com/demo/results/trainingS5F3UM-ER7/
"""

import time


def solution(A):
    """
    In this problem one could use a Caterpillar method to explore the search space
    for an optimal solution, however a simpler approach can be applied. Remember
    that the minimum slice length is 2!

    Consider the following array [4, 1, 1, 1, 1, 1, 8]
        1. Slice slice[1:2] => X[1,1] / len(X) = 1
        2. Slice slice[3:4] => X[1,1] / len(X) = 1
        3. Therefore slice[1:4] => X[1, 1, 1, 1] / len(X) = 1

    Every slice is made up of smaller slices of either 2 or 3. Therefore if all
    the subslices of 2 are minimal then the overall slice is minimal. If some
    subslice is not then it is not considered a candidate.

        4. [1, 1, 1, 8] can be split to [1, 1], [1, 8] with averages of 1 and 4.5
           Obviously we arent going to care about the average of 4.5
        5. [1, 1, 1, 8, 1] can be split into [1, 1, 1], [8, 1] giving 1 and 4.5
           Again we arent going to care about the average of 4.5
    """
    n = len(A)

    if n<3: # a small Array is a base case.
        return 0

    minimal = 10000000
    min_idx = 0

    # This loop cannot reach the final 2 indexes. But that is ok.
    for i in range(n-2):
        # Consider the first 2 elements
        two_sum = A[i] + A[i+1]
        # Then consider the 3rd added to the first 2
        three_sum = two_sum + A[i+2]
        # take the best average
        average = min( two_sum/2, three_sum/3 )

        # Both sub arrays started at index i
        if average < minimal :
            minimal = average
            min_idx = i
        # print(f'MinIndex:{min_idx} - Minimal:{minimal}')

    # Handle the final two indexes
    if (A[-1] + A[-2]) / 2 < minimal:
        min_idx = n-2
    # print(f'MinIndex:{min_idx} - Minimal:{minimal}')
    return min_idx


def solution_other(A):
    """
    See above
    """
    # Establish an average and a min idx
    avg = (A[0] + A[1]) / 2
    min_idx = 0
    
    # Looking at the previous 2 or 3 from A[2] onwards
    idx = 2
    while idx < len(A):

        cur = (A[idx-1] + A[idx] + A[idx-2])/3
        if cur < avg :
            avg = cur
            min_idx = idx-2
        
        cur = (A[idx-1] + A[idx])/2
        if cur < avg :
            avg = cur
            min_idx = idx-1
        idx += 1
    
    return min_idx


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (1, ([4, 2, 2, 5, 1, 5, 8],)),
        (7, ([4, 2, 2, 5, 1, 5, 8, 1, 1],)),
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