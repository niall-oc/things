# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

import time

def solution(A, B):
    n = len(A)
    if n < 2:
        return n
     
    segment_count = 1
    end = B[0]
     
    for i in range(1, n):
        if A[i] > end: # Must iterate over all planks under 'end' plank.
            end = B[i]
            segment_count += 1
            
     
    return segment_count

if __name__ == '__main__':
    tests = (
        (3, ([1, 3, 7, 9, 9], [5, 6, 8, 9, 10],)),
        
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        if args[0] is None:
            continue # just a speed test!
        try:
            # expected = brute_force_validator(*args)
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')