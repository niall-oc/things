
# -*- coding: utf-8 -*-
"""
Author: Niall O'Connor

# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/

You are going to build a stone wall. The wall should be straight and N meters 
long, and its thickness should be constant; however, it should have different 
heights in different places. The height of the wall is specified by an array 
H of N positive integers. H[I] is the height of the wall from I to I+1 meters 
to the right of its left end. In particular, H[0] is the height of the wall's 
left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such 
blocks are rectangular). Your task is to compute the minimum number of blocks 
needed to build the wall.

Write a function:

    def solution(H)

that, given an array H of N positive integers specifying the height of the wall, 
returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven 
blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].

# 100% solution https://app.codility.com/demo/results/trainingQB8TDX-9DP/
"""

import time


def solution(H):
    """
    if a block is higher than the last it goes on the stack.
    If a block is lower the stack is popped and counted 
    until the top block on the stack is lower than the current block.
    """
    stack = [-1]
    block_count = 0

    for height in H:
        if stack[-1] > height: # Pop blocks and count
            while stack[-1] > height:
                stack.pop()
                block_count += 1
                # print(f'blocks: {block_count} - stack: {stack} - height: {height}')

        if height > stack[-1]: # after all blocks are popped consider adding this block.
            stack.append(height)
        # print(f'blocks: {block_count} - stack: {stack} - height: {height}')
    return block_count + len(stack) -1


if __name__ == '__main__':

    tests = (
        # Test cases are in pairs of (expected, (args,))
        (7, ([8, 8, 5, 7, 9, 8, 7, 4, 8],)),
        (2, ([4, 4, 5, 5, 4, 4],)),
        (3, ([1, 2, 3],)),
        (1, ([2, 2, 2, 2],)),
        (1, ([1],)),
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