# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
def solution(A):
    # write your code in Python 3.6
    prefix_sum = [0] * len(A)
    avg = (A[0] + A[1]) / 2
    min_idx = 0
    
    idx = 2
    while idx < len(A):
        cur = (A[idx-2] + A[idx-1] + A[idx]) / 3
        if cur < avg :
            avg = cur
            min_idx = idx-2
        
        cur = (A[idx-1] + A[idx]) / 2
        if cur < avg :
            avg = cur
            min_idx = idx-1
        idx += 1
    
    return min_idx

