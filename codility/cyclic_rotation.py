# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
def solution(A, K):
    N = len(A)
    if N:
        K = K%N
        if K:
            return A[-K:]+A[:N-K]
    return A

