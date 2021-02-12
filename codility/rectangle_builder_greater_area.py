# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor
https://app.codility.com/programmers/lessons/91-tasks_from_indeed_prime_2016_challenge/rectangle_builder_greater_area/

100% solution https://app.codility.com/demo/results/trainingVE8WB6-82W/
"""
import time

def solve_brute_force(pairs, X, count):
    rectangles = {
        (pairs[x], pairs[y])
        for y in range(1, len(pairs))
            for x in range(0, y)
                if pairs[x] * pairs[y] >= X
    }
    # print(rectangles)
    count += len(rectangles)
    return count if count < 1000000000 else -1

def filter_pairs(A, X):
    """
    Pairs of sticks make opposite rectangle sides. Reduce pairs to one count.
    Special case is 4 or more sticks of same length, ie. a square!
        if they create a greater area than X count 1 rectangle.
    """
    A.sort()
    n = len(A); i = 1
    pairs = []; count = 0; square = 0
    while i < n:
        if A[i-1] != A[i]:
            i += 1
        else:
            hold = i - 1
            pairs.append(A[hold])
            while i<n and A[hold] == A[i]:
                i += 1
            else:
                if i - hold > 3:
                    # print(f'i - hold + 1 > 3 => {i} - {hold} + 1 > 3')
                    count += A[hold]**2 >= X
                    # print(f'A[hold]: {A[hold]}, count: {count}')
    return pairs, count

def solve_catepillar(pairs, X, count):
    """
    A sort of reverse catipillar contracting and counting the number of combinations.
    """
    start = 0; end = len(pairs) -1
    while start < end:
        while pairs[start] * pairs[end] >= X and start < end:
            count += end - start
            end -= 1
        start += 1
    return count if count < 1000000000 else -1

def solution(A, X):
    # First count squares and filter pairs
    pairs, count = filter_pairs(A, X)
    n = len(pairs)
    # print(pairs, count)   
    return solve_catepillar(pairs, X, count)
    
if __name__ == '__main__':
    tests = (
        #( expected, args )
        (2,  ([1, 2, 5, 1, 1, 2, 3, 5, 1], 5,)),
        (9, ([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8, 8], 9)),
        (11, ([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8, 8], 7)),
        (12, ([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 8, 8, 8, 8], 7)),
        (0,  ([], 0,)),
        (0,  ([1, 1, 1, 1, 1, 1], 4)),
        (1,  ([1, 1, 1, 1, 1], 1)),
        (0,  ([2, 2, 2], 4)),
        (1,  ([6, 6, 6, 6, 6, 6], 10)),
        (1,  ([5, 5, 5, 5, 5], 10)),
        (2,  ([1, 1, 7, 7, 7, 7, 7, 2, 2], 8)),
        (11, ([1, 1, 1, 2, 2, 2, 4, 4, 4, 3, 3, 3, 5, 6, 6, 6, 7, 8, 8, 8, 8, 8, 8], 7)),
        (1,  ([2, 1, 2, 5, 5], 9)),
        (1,  ([2, 1, 2, 1, 1], 2)),
        (1,  ([2, 1, 2, 2, 2], 4)),
        (1,  ([1, 1, 1000000000, 1000000000], 1000000000)),
        (6,  ([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 100, 100], 20)),
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
            print(f'ERROR {args} produced {res} when {expected} was expected!\n')

