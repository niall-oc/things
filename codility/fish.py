
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

You are given two non-empty arrays A and B consisting of N integers. 
Arrays A and B represent N voracious fish in a river, ordered downstream 
along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, 
then fish P is initially upstream of fish Q. Initially, each fish has a 
unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes 
of the fish. All its elements are unique. Array B contains the directions 
of the fish. It contains only 0s and/or 1s, where:

        0 represents a fish flowing upstream,
        1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) 
fish between them, they will eventually meet each other. Then only one 
fish can stay alive − the larger fish eats the smaller one. More precisely, 
we say that two fish P and Q meet each other when P < Q, B[P] = 1 and 
B[Q] = 0, and there are no living fish between them. After they meet:

        If A[P] > A[Q] then P eats Q, and P continues flowing downstream,
        If A[Q] > A[P] then Q eats P, and Q continues flowing upstream.

We assume that all the fish are flowing at the same speed. That is, fish 
moving in the same direction never meet. The goal is to calculate the 
number of fish that will stay alive.

For example, consider arrays A and B such that:
  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0

Initially all the fish are alive and all except fish number 1 are moving 
upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish 
number 3 and eats it too. Finally, it meets fish number 4 and is eaten by 
it. The remaining two fish, number 0 and 4, never meet and therefore stay 
alive.

Write a function:

    def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, 
returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, 
as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of A[] is an integer within the range [0..1,000,000,000];
        each element of B[] is an integer that can have one of the following values: 0, 1;
        the elements of A are all distinct.

# 100% solution https://app.codility.com/demo/results/trainingXUEZDW-AC7/
"""

import time


def solution(A, B):
    """
    Similar to the passing cars problem, the passing fish eat each other.
    Each downstream fish is pushed onto the downstream stack.
    Upstream fish are considered survivors if not eaten.
    When an upstream fish is encountered the downstream fish in its path are popped
    Each fish size is compared and teh smaller discarded.
    """
    downstream = []
    survivor = []
    for i in range(0, len(A)):
        print(f'pass {i}')
        if B[i]:  # If a fish is swimming downstream place him in that stack
            downstream.append(A[i])
            # print(f'survivor: <--{survivor}, downstream: {downstream}--> {A[i]} is A[{i}] -- Downstream encountered')
            continue
        elif downstream: # If the fish is swiming upstream and there are fish in the downstream 
            while downstream:
                if downstream[-1] < A[i]: # This fish is compared to the downstream fish.
                    # print(f'survivor: <--{survivor}, downstream: {downstream}--> {A[i]} is A[{i}]')
                    downstream.pop()
                else:
                    break # When this current fish is eaten by a downstream fish
            else:  #  All the downstream fish are eaten by the current upstream fish
                survivor.append(A[i])
                # print(f'survivor: <--{survivor}, downstream: {downstream}-->')
        else:  #  All the downstream fish are eaten
            survivor.append(A[i])
            # print(f'survivor: <--{survivor}, downstream: {downstream}-->')

        # print(f'survivor: <--{survivor}, downstream: {downstream}-->')  
    return len(survivor+downstream)


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (2, ([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])),
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