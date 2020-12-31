# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

#https://app.codility.com/programmers/lessons/17-dynamic_programming/min_abs_sum/

For a given array A of N integers and a sequence S of N integers from the set
{−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S)
from all possible values of val(A,S) for all possible sequences S of N integers
from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0,
which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].

90% solution https://app.codility.com/demo/results/trainingRBWTKF-FVG/
I'm convinced this is 100%!
"""
import time

def solution(A):
    """
    Sum of A is a measure of how far away from 0 you can go.
    Sum of A // 2 is how far you can go up and then back down.
    Positives on the way up and negatives on the way down.
    
    Array S is a red herring!
    """
    n = len(A)
    
    if n < 2: # quick base case
        return 0 if not n else A[0]
    
    # Set all values to absolute
    for i in range(n):
        A[i] = abs(A[i])

    # Working with a sorted array means we are working with the lowest 
    # possible value at each iteration which simplifies things.
    A.sort()

    maximum = sum(A)
    mid_point = maximum // 2

    balanced = not bool(maximum - (2*mid_point))
    
    left = 0
    right = 0

    # print(f'balanced: {balanced}, maximum: {maximum}, mid_point: {mid_point}, A:{A} ')

    for i in range(n-1, -1, -1):
        if right + A[i] <= mid_point:
            right += A[i]
        elif left + A[i] <= mid_point:
            left += A[i]
        else:
            if left < right:
                left += A[i]
            else:
                right += A[i]
    # print(f'left: {left}, right: {right}')

    return min(
        abs((maximum - right) - right),
        abs((maximum - left) - left) 
        )
    

if __name__ == '__main__':
    tests = (
        #( expected, args )
        (1, ([1, 3, 3, 4],)),
        (0, ([],)),
        (0, ([2,2],)),
        (1, ([-2,1],)),
        (0, ([2, 3, 2, 2, 3],)),
        (0, ([1, 5, -2, 5, 2, 3],)),
        (0, ([5, 5, 5, 4, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1],)),
        (1, ([20, 13, 3, 3, 3, 3],)),
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


