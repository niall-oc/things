# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/

def gen_fib(n):
    fn = [0] * n
    fn[1] = 1
    for i in range(2, n):
        fn[i] = fn[i-2] + fn[i-1]
    return fn

def solution(A, B):
    """
    The different arangements or combinations of adding 1 or 2 to get a number is also the fibonacci sequence!

    Consider the number of ways 5 can be created from using combinatinos 1 or 2:

        2 + (1+1+1), 2 + (2+1), 2 + (1+2)

    hmmm This looks like 2 + the 3 combinations you can make 3 from 1 or 2.

        1 + (1+1+1+1), 1 + (2+2), 1 + (1+2+1), 1 + (2+1+1), 1 + (1+1+2)

    and that looks like 1 + the 5 combinations you can make 4 from!

    8 combinations = 3 combinations + 5 combinations!

    so f(n) = f(n-2) + f(n-1). . . !

    Thats the fibonacci sequence!  But 0, 1 and 2 are special cases

    0 = 0

    1 = 1 + (0)  and 2+??  you cannot use 2 at all.  Technically thats a total of 0 combinations but the answer is 1
    2 = 2 + (0) and 1+(1)  Technically thats a total of 1 combinations ( after considering having 1 or 2 at the start)

    While both those cases are fibonacci correct they don't fit the problem exactly.

    The answer is in fact:  The number of ways to climb a ladder ( in 1 or 2 step combinations) is the same as fib(n-1)
    That implies you must shift the offset your fn series to get the correct number!

    """

    # A and B are equal length
    n = len(A)

    # any number in a can be between 0 and n
    fn_series = gen_fib(n+2)[1:] # Note. .  0, 1, and 2 are special, so shift the array and make it long enough for fn_series[A[i]] to succeed.

    # The result is a list of numbers representing fib(A[i]) % 2^B[i].for all i between 0 and n.

    # precompute B for speed on large arrays.

    pB = {i: 2**i for i in range(1, 31)}

    result = [fn_series[A[i]]&(pB[B[i]]-1) for i in range(n)]
    # https://stackoverflow.com/questions/6670715/mod-of-power-2-on-bitwise-operators/6670766#6670766
    # Best explains why bitwise & is faster than mod for this calculation.
    return result



if __name__ == '__main__':
    tests = (
        ([2, 3, 2, 1] , ([2, 3, 2, 4], [2, 2, 3, 2])),
    )
    for expected, args in tests:
        res = solution(*args)
        try:
            assert(expected == res)
        except AssertionError as e:
            print(expected, args, res)