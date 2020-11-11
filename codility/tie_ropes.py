# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

import time

def solution(K, A):
    rope_count = 0
    this_rope = 0
    for part in A:
        this_rope += part
        if this_rope >= K:
            rope_count +=1
            this_rope = 0
 
    return rope_count

if __name__ == '__main__':
    tests = (
        (3, (4, [1,2,3,4,1,1,3],)),
        (5, (5, [1,2,3,4,1,1,1,3,5,6],)),
        (1, (1, [1],)),
        (0, (2, [1],)),
        (5, (4, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3],)),
        (5, (5, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 3],)),
        (4, (5, [5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3],)),
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