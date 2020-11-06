# https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct

import time

def solution(A):
    return len({abs(i) for i in A})

if __name__ == '__main__':
    tests = (
        (5, ([-5, -3, -1, 0, 3, 6],)),
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')