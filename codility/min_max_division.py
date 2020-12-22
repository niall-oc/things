# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/

You are given integers K, M and a non-empty array A consisting of N integers.
Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of
the block is any integer between 0 and N. Every element of the array should
belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of
empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal
large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers,
returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].

100% solution #https://app.codility.com/demo/results/trainingDR8Q7H-ERS/
O(N*log(N+M))
"""
import time

def is_valid_minimal_limit(A, num_blocks, sum_slice_limit):
    """
    Scans Array A summing values until minimal_limit is reached.  Array A cannot
    be divided into more than num_blocks.  If the parameters given cannot succeed
    then a False is returned.
    """
    block_count = 0
    block_sum = 0

    for number in A:
        new = block_sum + number
        if new <= sum_slice_limit: # We have not breached the block sum limit
            block_sum = new
        else:                      # We have breached the block sum limit
            block_count += 1
            block_sum = number
        if block_count >= num_blocks:
            return False
    return True

def binary_search(A, num_blocks):
    """
    When array is divided into num_blocks the sum of each block searched to find
    the minimal highest block value.
    """
    sum_slice_min = max(A)
    sum_slice_max = sum(A)

    while sum_slice_min <= sum_slice_max:
        sum_slice_mid = (sum_slice_min + sum_slice_max) // 2
        #print(sum_slice_mid)
        if is_valid_minimal_limit(A, num_blocks, sum_slice_mid):
            sum_slice_max = sum_slice_mid - 1 # Search the lower half of the space
        else:
            sum_slice_min = sum_slice_mid + 1 # Search the upper half of the space
    
    return sum_slice_min

def solution(K, M, A):
    # Using M as the assumed max value of array A doesn't work!!!
    return binary_search(A, K)

if __name__ == '__main__':
    tests = (
        (6, (3, 5, [2, 1, 5, 1, 2, 2, 2],)),
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