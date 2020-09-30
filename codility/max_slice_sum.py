# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
def solution(A):
    base = min(A)
    ending = 0
    max_slice = base
    for a in A:
        ending = max(base, ending + a, a)
        max_slice = max(max_slice, ending)
    return max_slice

