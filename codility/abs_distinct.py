# https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct

import time

def solution_p(A):
    """
    This is why I love python!  100% answers in one line.  It is taking the p*** though!
    """
    return len({abs(i) for i in A})

def solution(A):
    """
    https://app.codility.com/demo/results/trainingZY7TF6-PNU/
    """
    n = len(A)

    if n == 1:
        return n
    elif n == 2:
        return 1 if abs(A[0]) == abs(A[1]) else 2

    for i in range(n):
        if not A[i]:
            break
        else:
            A[i] = abs(A[i]) # remove minus sign

    A.sort()
    i = 0; pos = 1; distinct_count = 1
    # print(A)
    while i < n-1:
        # print(f'iteration : {i}')
        # print(f'i:{i}, pos{pos}, distinct_count : {distinct_count} - pre  while') 
        # print(f'{A[i]} == {A[pos]} : {A[i] == A[pos]}')
        while pos < n and A[i] == A[pos]:
            pos += 1
        # print(f'i:{i}, pos{pos}, distinct_count : {distinct_count} - post while') 
        if pos - i == 1:
            distinct_count += 1
            i = pos; pos += 1
        else:    
            i = pos-1
        # print(f'i:{i}, pos{pos}, distinct_count : {distinct_count} - post increment')

    return distinct_count


if __name__ == '__main__':
    tests = (
        (5, ([-5, -3, -1, 0, 3, 6],)),
        (1, ([1]*20,)),
        (3, ([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3],)),
        (5, ([-4,-3,-2,-1,0,1,2,3,4],)),
        (1, ([0,0],)),
        (2, ([-2,-1],)),
        (1, ([0],)),
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