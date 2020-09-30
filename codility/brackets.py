# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
def solution(S):
    stack = []
    openers, closers = '{[(', '}])'
    for char in S:
        if char in openers:
            stack.append(char)
        else:
            # if there is a mismatch or an empty stack for a closing char its a fail
            if stack:
                sc = stack.pop()
                if openers.index(sc) != closers.index(char):
                    return 0
            else:
                return 0
    if stack:  # stack should be empty
        return 0
    return 1

