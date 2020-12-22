# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/

You are given two non-empty arrays A and B consisting of N integers. These
arrays represent N planks. More precisely, A[K] is the start and B[K] the end of
the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array
represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that
A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the
planks are nailed. In other words, you should find a value J such that all
planks will be nailed after using only the first J nails. More precisely, for
every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I]
such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the
planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a
non-empty array C consisting of M integers, returns the minimum number of nails
that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].

100% solution #https://app.codility.com/demo/results/trainingQDJYXJ-K5E/
O((N + M) * log(M))
"""
import time

def solution_brute_force(A, B, C):
    """
    Scan the arrays and position all planks.

    Follow the link for the results of this approach.
    # https://app.codility.com/demo/results/training9CNGYJ-2HJ/
    """
    used = 0
    for i in range(len(C)): # for each nail
        # check we have not removed all planks
        if not A:
            break
        
        # find all planks it hits
        removed_planks = sorted([j for j in range(len(A)) if A[j] <= C[i] and C[i] <= B[j]], reverse=True)
        
        if removed_planks:
            # removed nailed planks
            for j in removed_planks:
                del A[j]
                del B[j]
        used += 1
        # print(C[i], removed_planks, used)
    return -1 if A else used

def find_nail(plank, C):
    """
    Binary search of C for nail that fits plank.
    C must be sorted!
    """
    BEGIN_IDX = 0
    END_IDX = 1
    lower = 0
    upper = len(C)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if C[mid] < plank[BEGIN_IDX]:
            lower = mid + 1
        elif C[mid] > plank[END_IDX]:
            upper = mid - 1
        else: # Therefore plank[BEGIN_IDX] <= C[mid] and C[mid] <= plank[END_IDX]
            return True
    return -1

def find_plank(nail, planks):
    """
    planks is an array of pairs (begin, end) for each plank.
    planks is sorted by start position of planks
    """
    if not planks:
        return -1 # empty planks
    BEGIN_IDX = 0
    END_IDX = 1
    lower = 0
    upper = len(planks)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if planks[mid][BEGIN_IDX] > nail:
            upper = mid - 1
        elif planks[mid][END_IDX] < nail:
            lower = mid + 1
        else: # nail hits plank[mid]
            return mid # return this plank id so we can pop the plank
    return -1


def solution(A, B, C):
    """
    Strategy is to sort the planks first. Then scan the nails and do the following.
    For each nail perform a binary search for a plank.
        if plank found then pop plank then search again until the nail hits no more planks.
    The plank list should diminish until it hits zero meaning we have found the minimum number of nails needed
    If any planks remain then return -1
    """

    if max(B) < min(C) or max(C) < min(A):
        return -1 # no nail can hit that plank

    planks = sorted(zip(A,B))

    for i in range(len(C)):
        nail = C[i]
        p_idx = find_plank(nail, planks)
        # print(f'idx{i} nail at pos {nail}, matched {p_idx}, in {planks}')
        while p_idx > -1:
            del planks[p_idx]
            p_idx = find_plank(nail, planks)
            # print(f'idx{i} nail at pos {nail}, matched {p_idx}, in {planks}')
        if not planks:
            # print('NO PLANKS', i+1)
            return i+1 # the index of the nail that removed the last plank.

    return -1 # else we couldn't remove all planks

if __name__ == '__main__':
    tests = (
        #(4, ([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])),
        #(1, ([1], [2], [2])),
        #(-1, ([2], [2], [1])),
        (1, ([1]*100, [4]*100, [2]*1000)),
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