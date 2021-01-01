# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

#



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


"""

import time

def solution(A):
    """
    Add every possible value greater than -1 and when you encounter a negative
    stretch try to take the best values on each roll.
    """
    n = len(A)

    if n == 2:
        return sum(A)

    max_score = A[0]
    lowest_value = -1000001
    limit = n-1
    i=1
    print(f'A:{A}')
    while i < limit:
        print(f'max_score: {max_score}, i: {i}')
        if A[i] > 1:
            max_score += A[i]
            print(f'Positives and break max_score: {max_score}')
        else:
            negatives = lowest_value; positives=False
            d = 0; last = i
            # Examine all dice rolls
            while i+d < limit and d < 7:   
                # if we don't find a positive score, then determine the best negative
                print(f'negatives: {negatives}, A[i+d]: {A[i+d]}')
                if A[i+d] < 0:
                    negatives = max(A[i+d], negatives)
                    last = i+d
                else:
                    max_score += A[i+d]
                    i += d
                    positives = True
                    print(f'Positives and break max_score: {max_score}')
                    break
                d += 1
            if not positives:
                max_score += negatives
                i = last
        i += 1
    return max_score + A[-1]


if __name__ == '__main__':
    tests = (
        #( expected, args )
        (8, ([1, -2, 0, 9, -1, -2],)),
        (4, ([-2, 5, 1],)),
        (-12, ([0, -4, -5, -2, -7, -9, -3, -10],)),
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