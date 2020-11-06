# https://codility.com/media/train/13-CaterpillarMethod.pdf

import time
import random

def brute_force_validator(A):
    n = len(A)
    A.sort()
    result = 0
    for z in range(2, n):
        for y in range(1, z):
            for x in range(0, y):
                if A[x]+A[y] > A[z]:
                    result += 1
    return result

def ncr(r, n):
    if r == n:
        return 1
    elif r + 1 == n:
        return n
    elif r > n:
        return 0
    else:
        return r * ncr(r, n-1)

def solution(A):
    n = len(A)
    A.sort()
    result = 0

    for x in range(0, n-2): # A[z] always being the largest side of the triangle if A is 
        # print(f'Iteration {x}')
        y = x + 1
        z = x + 2
        # With A[z] being the largest side of the triangle, (A[x] + A[y]) > A[z] only needs proof
        while z<n:
            if A[x] + A[y] > A[z]:
                result += z - y
                z += 1
                # print(f'[{x}, {y}, {z-1}->{z}] - TRIANGLE  result is : {result}')
            
            # When the above condition fails every combination of x < y < z-1  is a triangle
            elif y < z - 1:
                y += 1
            else:
                y += 1; z += 1
    return result


if __name__ == '__main__':
    tests = (
        (4, ([10, 2, 5, 1, 8, 12],)),
        (3, ([3, 3, 5, 6],)),
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
            # print(f'ERROR {args} produced {res} when {expected} was expected!')
            pass