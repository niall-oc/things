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
    """
    Given an array A of len n.
    From index last_pos which numbers in fn jump to a leaf?
    returns list: set of indexes with leaves.
    """
    paths = []
    for f in fn:
        new_pos = last_pos + f
        if new_pos == n or (new_pos < n and A[new_pos]):
            paths.append(new_pos)
    return paths


def solution(A):
    n = len(A)
    if n < 3:
        return 1

    # A.append(1) # mark final jump
    fn = sorted(gen_fib(100000)[2:]) # Fib numbers with 0, 1, 1, 2..  clipped to just 1, 2..
    # print(fn)
    paths = {0:set([-1])} # locate all the leaves that are one fib jump from the start position.
    result = 0

    jump = 1
    while True:
        # Considering each of the previous jump positions - How many leaves from there are one fib jump away
        new_jumps =  set([idx for pos in paths[jump-1] for idx in new_paths(A, n, pos, fn)])

        # no new jumps means game over!
        if not new_jumps:
            break
        # else update the paths
        paths[jump] = new_jumps

        # If there was a result in the new jumps record that
        if n in new_jumps:
            return jump
        jump += 1

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