# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
def solution(A):
    n = len(A)
    max_starts = [0]*n
    max_ends = [0]*n
    
    max_sum = 0
    for i in range(n-2, 0, -1):          
        max_sum = max(0, max_sum+A[i])
        max_ends[i] = max_sum
    
    max_sum = 0
    for i in range(1, n-1):          
        max_sum = max(0, max_sum+A[i])
        max_starts[i] = max_sum
    
    max_sum = 0
    for i in range(0, n-2):
        max_sum = max(max_sum, max_starts[i] + max_ends[i+2])

    return max_sum;

