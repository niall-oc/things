
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is 
properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given 
S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".

# 100% solution https://app.codility.com/demo/results/trainingNUEHPR-QAA/
"""

import time


def solution(S):
    """
    Opening parenthesis are pushed and closing parenthesis pop.
    If the stack is empty prematurely there are too many closing brackets.
    If the stack is populated at the end there are too many opening brackets.
    """
    stack = []
    opener, closer = '(', ')'
    for char in S:
        if char == opener:
            stack.append(char)
        else:
            # if there is a mismatch or an empty stack for a closing char its a fail
            if not stack:
                return 0
            else:
                stack.pop()
    return 0 if stack else 1


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (1, ("(()(())())",)),
        (0, ("())",)),
    )

    for expected, args in tests:
        # record performance of solution
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')

        if args[0] is None:
            continue # This is just a speed test

        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')