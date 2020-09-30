# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
def solution(N):
    # write your code in Python 3.6
    R = int(N**.5)
    result = 0
    
    for i in range(1, R+1):
        if not N%i:
            result = result + 2
    
    if R*R == N:
        result = result - 1
        
    return result


