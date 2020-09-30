# https://app.codility.com/programmers/lessons/6-sorting/triangle/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    i = 2
    if N > i:
        while i < N:
            if A[i-2] + A[i-1] > A[i]:
                return 1
            i+=1
    return 0

