# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/

A game for one player is played on a board consisting of N consecutive squares,
numbered from 0 to N − 1. There is a number written on each square. A non-empty
array A of N integers contains the numbers written on the squares. Moreover, 
some squares can be marked during the game.

At the beginning of the game, there is a pebble on square number 0 and this is 
the only square on the board which is marked. The goal of the game is to move 
the pebble to square number N − 1.

During each turn we throw a six-sided die, with numbers from 1 to 6 on its 
faces, and consider the number K, which shows on the upper face after the die 
comes to rest. Then we move the pebble standing on square number I to square 
number I + K, providing that square number I + K exists. If square number I + K 
does not exist, we throw the die again until we obtain a valid move. Finally, 
we mark square number I + K.

After the game finishes (when the pebble is standing on square number N − 1), 
we calculate the result. The result of the game is the sum of the numbers 
written on all marked squares.

For example, given the following array:
    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2

one possible game could be as follows:

        the pebble is on square number 0, which is marked;
        we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
        we throw 5; the pebble does not move, since there is no square number 8 on the board;
        we throw 2; the pebble moves to square number 5; we mark this square and the game ends.

The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8. 
This is the maximal possible result that can be achieved on this board.

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the maximal result that 
can be achieved on the board represented by array A.

For example, given the array
    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2

the function should return 8, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].
( not always finding the best score ahead :-/ )
100% solution https://app.codility.com/demo/results/trainingG5FNV9-7SY/
50%  solution https://app.codility.com/demo/results/trainingFC9NZG-ERW/
O(n)
"""

import time

def solution_old(A):
    """
    Incrimentally walk the list. From any index in the list we want
    the dice roll to support the maximum score. That implies the following.
    
    1. Consider positive cases in the next 6 indexes. We don't want to miss any
       therefore we take the nearest positive value and make that our index.
    2. Consider negative cases in the next 6 indexes. We want to jump to the
       nearest highest minimum value.
    """
    n = len(A)

    if n == 2:
        return sum(A)

    max_score = A[0]  # set max_score to our starting score
    limit = n-1; i=1; # working from index 1 to the second last index
    print(f'\nA:{A}, i{i}: limit:{limit}')
    
    while i < limit:
        print(f'-BEGIN- max_score:{max_score}, i:{i}')
        # Look through the next 6 values and track the highest furthest negative
        # OR break on the first positive.
        highest_negative = -100000001
        lowest_positive_idx = highest_negative_idx = 0
        end = min(i+6, limit)
        for bn in range(i, end):
            # Record a negative as we encounter it.
            if A[bn] < 1 and A[bn] >= highest_negative:
                # in the case of their only being negative numbers ahead
                # we must find the furthest highest index.
                highest_negative = A[bn]
                highest_negative_idx = bn
                print(f'NEGATIVE - i:{i}, end:{end}, A[{bn}]: {A[bn]}')
            elif A[bn] > 0:
                # In a scoring case leave loop and proceed to score
                lowest_positive_idx = bn
                print(f'POSITIVE - i:{i}, end:{end}, A[{bn}]: {A[bn]}')
                break
        
        # determine the best way forward.
        if lowest_positive_idx:
            i = lowest_positive_idx
        elif i+6 > limit: # The end is in sight!
            # There were no positive numbers in our scan but we can finish.
            print('The end is in sight!')
            break
        else:
            i = highest_negative_idx
        max_score += A[i]
        i += 1
        print(f'--END-- max_score:{max_score}, i:{i}')
    return max_score + A[-1]

def solution(A):
    """
    On any square ask, what is the best exit score from any of the previous 6
    squares that I can be reached from? And what wil me exit score be?

          +-----------------------------------------------+
    entry | 0 | 0 | 0 | 0 | 0 | 0 | 0 |-2 |-4 | -4| 5 | 5 |
    ------+-----------------------------------------------+
    value | 0 |-2 |-9 |-9 |-9 |-9 |-9 |-2 |-2 | 9 | 0 |-2 |
    ------+-----------------------------------------------+
    exit  | 0 |-2 |-9 |-9 |-9 |-9 |-9 |-4 |-6 | 5 | 5 | 3 |
    ------+-----------------------------------------------+
    """
    n = len(A)
    MAX_ROLL = 6 # 6 sided dice means we can look back a max of 6 spaces.
    exit_score = [A[0]] * n  # Set all exit scores to start score
    for i in range(1, n):
        # At each point slice the previous 6 exit scores and choose the best
        spread = exit_score[max(i-MAX_ROLL, 0):i]
        # print(spread, max(spread))
        exit_score[i] = A[i] + max(spread)
    return exit_score[-1]

if __name__ == '__main__':
    tests = (
        #( expected, args )
        (8, ([1, -2, 0, 9, -1, -2],)),
        (4, ([-2, 5, 1],)),
        (-12, ([0, -4, -5, -2, -7, -9, -3, -10],)),
        (-6, ([0, -2, -2, -9, -9, -9, -9, -9, -2, -9, -2, -2, -9, -2, -2],)),
        (20, ([0, -2, -9, -9, -2, 7, 9, 1, 3],)),
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