# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/

import time

def factorial(n):
    # check if the number is negative, positive or zero
    if n < 0:
        raise ValueError("Sorry, factorial does not exist for negative numbers")
    elif not n:
        return 1 # zero has a factorial of one
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial*i
        return factorial

def ncr(r, n):
    return factorial(n) // (factorial(r)*factorial(n-r))

def count_slices(n):
    total_slices = 0
    if n < 2:  
        total_slices += n
    else:
        total_slices += ncr(2, n) + n
    print(f'slice_length {n} produced {total_slices} slices')
    return total_slices

def solution(M, A):
    """
    The catepilar expands as it consumes new unique numbers. 
    As it grows the combination of slices contained within the range start to end is counted.
    When a duplicate is encountered the catepilar contracts until the set is unique.

    https://app.codility.com/demo/results/training69FPP4-SFG/
    """
    n = len(A)

    if not n: # empty list
        return 0

    limit = 1000000000 # No more slices than this should be counted
    start = 0
    end = 0
    total_slices = 0
    duplicate = [0] * (M+1) # use an array to efficently mark numbers encountered

    while end < n and start < n: # don't overrun indexes

        while end < n and not duplicate[A[end]]: # expand when no duplicates found
            # print(f'A[{start}:{end}] -> {A[start:end+1]}')
            total_slices += end-start+1 # By factoring in the 1 this happens to be nCr(2, end-start)!
            duplicate[A[end]] = 1
            end += 1
            if total_slices > limit:
                return limit
        else:
            while end < n and start< n and A[start] != A[end]: # Move forward until start matches end
                duplicate[A[start]] = 0
                start += 1
            # Now move past the duplicate. This handles cases like [1, 1, 1] by counting [1], [1] and [1] as slices.
            duplicate[A[start]] = 0
            start += 1

    return total_slices


if __name__ == '__main__':
    tests = (
        (9, (6, [3, 4, 5, 5, 2],)),
        (5, (2, [1, 1, 1, 1, 1],)),
        (33, (10, [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9],)),
        (39, (10, [1, 2, 3, 4, 5, 6, 2, 8, 6, 7],)),
        (0, (1, [],)),
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