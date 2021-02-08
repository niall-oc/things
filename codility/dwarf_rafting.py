# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor
# https://app.codility.com/programmers/lessons/91-tasks_from_indeed_prime_2016_challenge/dwarfs_rafting/

100% solution https://app.codility.com/demo/results/training59XKKN-HAW/
"""
import time

# Alphabet indexes ( 0 indexed )
AB = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
NUMBER=0; LETTER=1 # Useful indexes for exploding each coordinate

def parse_indexes(S):
    # both number and letter component are zero indexed
    # String indexes are very important here!
    return set([(int(s[0:-1])-1, AB[s[-1]],) for s in S.split(' ') if s])

def count_half(A, mid_point, INDEX):
    lower = len([i for i in A if i[INDEX] <= mid_point])
    upper = len([i for i in A if i[INDEX] > mid_point])
    return lower, upper

def count_quadrants(A, N):
    mid_point = (N//2) - 1 # The length of a square side, halved
    FL, FR = count_half([a for a in A if a[NUMBER] <= mid_point], mid_point, LETTER)
    BL, BR = count_half([a for a in A if a[NUMBER] > mid_point], mid_point, LETTER)
    return FL, FR, BL, BR

def solution(N, S, T):
    # The constants
    barrels = parse_indexes(S) # Barrels
    dwarves = parse_indexes(T) # Dwarves
        
    barrel_count = dict(zip(('FL', 'FR', 'BL', 'BR'), count_quadrants(barrels, N)))
    dwarve_count = dict(zip(('FL', 'FR', 'BL', 'BR'), count_quadrants(dwarves, N)))
    
    quadrant_size = (N*N) // 4
    free_seats = {
        'FL' : quadrant_size - barrel_count['FL'] - dwarve_count['FL'],
        'FR' : quadrant_size - barrel_count['FR'] - dwarve_count['FR'],
        'BL' : quadrant_size - barrel_count['BL'] - dwarve_count['BL'],
        'BR' : quadrant_size - barrel_count['BR'] - dwarve_count['BR'],
    }
    
    max_seats = {
        'FL' : quadrant_size - barrel_count['FL'],
        'FR' : quadrant_size - barrel_count['FR'],
        'BL' : quadrant_size - barrel_count['BL'],
        'BR' : quadrant_size - barrel_count['BR'],
    }
    
    # Opposite corners must balance. If any diagonal holds more dwarves than there are
    # barrel free spaces on its opposing diagonal the raft is not possible to balance!
    fswish = min(max_seats['FR'], max_seats['BL']) # / diagonal
    fswosh = min(max_seats['FL'], max_seats['BR']) # \ diagonal
    dswish = max(dwarve_count['FR'], dwarve_count['BL']) # / diagonal
    dswosh = max(dwarve_count['FL'], dwarve_count['BR']) # \ diagonal
    #print(f'dwarve_count: {dwarve_count}, max_seats: {max_seats}, free_seats: {free_seats}')
    #print(f'fswish < dswish or fswosh < dswosh => {fswish} < {dswish} or {fswosh} < {dswosh}')
    if fswish < dswish or fswosh < dswosh:
        return -1
    else:
        seats_swish = (fswish * 2) - (dwarve_count['FR'] + dwarve_count['BL'])
        seats_swosh = (fswosh * 2) - (dwarve_count['FL'] + dwarve_count['BR'])
        return seats_swish + seats_swosh # all free balancing seats across both diagonals

if __name__ == '__main__':
    tests = (
        #( expected, args )
        (6,  (4, "1B 1C 4B 1D 2A", "3B 2D",)),
        (16, (4, "", "",)),
        (4,  (2, "", "",)),
        (2,  (2, '2A', '',)),
        (-1, (2, '1A', '2B',)),
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
