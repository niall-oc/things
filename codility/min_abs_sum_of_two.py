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

    head = n-1
    tail = 0
    m = 2000000000
    while tail <= head:
        m = min(m, abs( A[tail] + A[head] ))
        if abs(A[tail]) > abs(A[head]) : # This will decide how to move the catepillar
            tail +=1
        else:
            head -= 1
    return m

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