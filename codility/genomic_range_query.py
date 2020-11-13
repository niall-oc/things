
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

A DNA sequence can be represented as a string consisting of the letters A, C, G 
and T, which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. Nucleotides of types 
A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going 
to answer several queries of the form: What is the minimal impact factor of 
nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting 
of N characters. There are M queries, which are given in non-empty arrays P and Q, 
each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find 
the minimal impact factor of nucleotides contained in the DNA sequence between 
positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        * The part of the DNA between positions 2 and 4 contains nucleotides 
          G and C (twice), whose impact factors are 3 and 2 respectively, so 
          the answer is 2.
        * The part between positions 5 and 5 contains a single nucleotide T, 
          whose impact factor is 4, so the answer is 4.
        * The part between positions 0 and 6 (the whole string) contains all 
          nucleotides, in particular nucleotide A whose impact factor is 1, 
          so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty 
arrays P and Q consisting of M integers, returns an array consisting of M integers 
specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.


# 100% solution https://app.codility.com/demo/results/trainingUV9GTG-U3W/
"""

import time

def solution(S, P, Q):
    """
    Simply scan the DNA string and record 3 distinct slopes for the increase
    of A, C, G.  T is assumed to occur if the other 3 don't occur.

    Then examine the start and end index each sequence.
        if A[end] - A[begin] > 0 an a occured and we can say that is the minimum occurence
        if C[end] - C[begin] > 0   "  "
        if G[end] - G[begin] > 0   "  "
        else T must have occured.

    """
    n = len(S)
    
    # create arrays to track occurences of characters
    A = [0] * (n+1)
    C = [0] * (n+1)
    G = [0] * (n+1)

    # scan each character
    for i in range(n):
        A[i+1] = A[i] + (S[i]=='A') # A i+1 will record and increase in A
        C[i+1] = C[i] + (S[i]=='C') # A i+1 will record and increase in A
        G[i+1] = G[i] + (S[i]=='G') # A i+1 will record and increase in A
    
    m = len(P)
    results = [0] * m

    for i in range(m):
        start = P[i];  end = Q[i] + 1
        # A_occured, C_occured, G_occured = A[end] - A[start], C[end] - C[start], G[end] - G[start]
        if A[end] - A[start]:   # If numbers are not identical an A occured
            results[i] = 1      # Record weight of an A in results[i]
        elif C[end] - C[start]: # If numbers are not identical an C occured
            results[i] = 2      # Record weight of an C in results[i]
        elif G[end] - G[start]: # If numbers are not identical an G occured
            results[i] = 3      # Record weight of an G in results[i]
        else:
            results[i] = 4      # Record weight of an T in results[i]

    return results

if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        ([2, 4, 1], ('CAGCCTA', [2, 5, 0], [4, 5, 6],)),
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