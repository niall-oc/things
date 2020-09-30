# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
def max_slice_prof(A, start, end):
    ending = 0
    max_slice = 0
    for i in range(start, end):
        ending = max(0, ending + A[i])
        max_slice = max(max_slice, ending)
    return max_slice

def solution(A):
    n = len(A)
    moves =[0]*n
    
    for i in range(1, n):
        moves[i] = A[i] - A[i-1]
    return max_slice_prof(moves, 0, n)

