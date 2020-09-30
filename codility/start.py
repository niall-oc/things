# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/start/
def solution(A):
    # write your code in Python 3.6
    MAX = 1000000000
    weight = sum(A)

    i = 0
    passes = 0
    while i < len(A) and weight:
        if not A[i]: # a 0 encountered
            passes += weight
        else:
            weight -= 1
        
        if passes > MAX:
            return -1
        i+=1
    
    return passes

