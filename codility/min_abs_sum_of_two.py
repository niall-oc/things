# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/
import time

def brute_force_validator(A):
    n = len(A)
    A.sort()
    minimal = 2000000000
    for low in range(n):
        for high in range(n):
            minimal = min(abs(A[low] + A[high]), minimal)
    return minimal

def solution(A):
    n = len(A)
    A.sort()

    if n==1:
        return abs( A[0] + A[0] )

    head = 0
    tail = 0
    m = minimal = abs( A[tail] + A[head] )
    # Walk along the sorted array and search for a minimal
    for tail in range(n):

        m = abs( A[tail] + A[head] )
        # print(f'{m} = abs( {A[tail]} + {A[head]} ) [{tail}:{head}] -> {A[tail:(head+1)]}')
        while m <= minimal and head < n-1:
            head += 1
            m = abs( A[tail] + A[head] )
        
        minimal = min(m, minimal)

    return minimal

if __name__ == '__main__':
    tests = (
        (1, ([1, 4, -3],)),
        (3, ([-8, 4, 5, -10, 3],)),
        (0, ([0],)),
        (4, ([2, 2],)),
        (6, ([8, 5, 3, 4, 6, 8],)),
        # (None, ([random.randint(1, 10000) for i in range(100)],)),
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