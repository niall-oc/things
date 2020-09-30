# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
def solution(A, B, K):
    # if A, B,K are already valid inputs!
    return ((B // K) + 1) - ((A + K -1) // K)


