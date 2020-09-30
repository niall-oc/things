# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
def solution(N):
    # write your code in Python 3.6
    max_int_root = int(N**.5)
    
    # is it a square?
    if max_int_root**2 == N:
        return 4*max_int_root
    
    while N%max_int_root:
        max_int_root -= 1 # find the next highest commond divisor.
        
    B = N//max_int_root

    return 2 * (B+max_int_root)

