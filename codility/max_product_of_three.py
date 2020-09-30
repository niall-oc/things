# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    l = len(A)
    if l == 3:
        return A[0] * A[1] * A[2]
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

