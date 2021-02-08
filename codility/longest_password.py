# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/start/

You would like to set a password for a bank account. However, there are three
restrictions on the format of the password:

it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
there should be an even number of letters;
there should be an odd number of digits.

You are given a string S consisting of N characters. String S can be divided
into words by splitting it at, and removing, the spaces. The goal is to choose
the longest word that is a valid password. You can assume that if there are K
spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of
them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is
"pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid
password, because "?" is not an alphanumerical character and "test" contains an
even number of digits (zero).

Write a function:

def solution(S)

that, given a non-empty string S consisting of N characters, returns the length
of the longest word from the string that is a valid password. If there is no
such word, your function should return −1.

For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7,
as explained above.

Assume that:

N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces.
In your solution, focus on correctness. The performance of your solution will
not be the focus of the assessment.

100% solution https://app.codility.com/demo/results/training3G5XYJ-E9C/

"""

import time

def solution(S, delimiter=' '):
    max_len = 0
    for passwd in S.split(delimiter):
        if passwd:
            char = digit = bad = 0
            for c in passwd:
                if c.isalpha():
                    char += 1
                elif c.isdigit():
                    digit += 1
                else:
                    bad = True
            if not bad and not char%2 and digit%2:
                max_len = max(max_len, len(passwd))
                
    return max_len or -1

if __name__ == '__main__':
    tests = (
        #( expected, args )
        (7, ("test 5 a0A pass007 ?xy1",)),
        (-1, ("a",)),
        (-1, ("",)),
    )

    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()

        if expected is None:
            print(f'SPEED-TEST {len(args[0])} args finished in {toc - tic:0.8f} seconds')
            continue # This is just a speed test
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!\n')
