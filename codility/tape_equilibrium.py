# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
def solution(A):
    left = A[0]
    right = sum(A[1:])
    min_difference = abs(left - right)
    for index in range(1, len(A)-1):
        left += A[index]
        right -=A[index]
        diff = abs(left - right)
        if diff < min_difference:
            min_difference = diff
    return min_difference

