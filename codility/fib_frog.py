# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog

def gen_fib(n):
    fn = [0,1]
    i = 2
    s = 2
    while s < n:
        s = fn[i-2] + fn[i-1]
        fn.append(s)
        i+=1
    return fn

def new_paths(A, n, last_pos, fn):
    paths = []
    for f in fn:
        new_pos = last_pos + f
        if new_pos == n or (new_pos < n and A[new_pos]):
            paths.append(new_pos)
    return paths


def solution(A):
    n = len(A)
    #print(n, list(enumerate(A)))
    if n < 3:
        return 1

    fn = sorted(gen_fib(100000)[2:])
    #print(fn)
    # a queue of paths that are still solvable!
    paths = {-1: 0}
    iteration = 1
    while True:
        #print(paths)
        cp = []
        for lp, it in paths.items():
            np = new_paths(A, n, lp, fn)
            #print(iteration, lp, np)
            cp.extend(np)
        if not cp:
            break
        paths = {p: min(iteration, paths.get(p, 10000000)) for p in cp}
        #print(paths)
        iteration += 1
    if n in paths:
        return paths[n]
    return -1

if __name__ == '__main__':
    tests = (
        (3, ([0,0,0,1,1,0,1,0,0,0,0],)),
        (1, ([],)),
        (1, ([1],)),
        (1, ([0],)),
        (1, ([1, 1],)),
        (2, ([1,1,1],)),
        (5, ([0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0],)),
        (3, ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],)),
        (3, ([0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0],)),
        (-1, ([0, 1, 0, 0, 0],)),
    )
    for expected, args in tests:
        res = solution(*args)
        try:
            assert(expected == res)
        except AssertionError as e:
            print(expected, args, res)