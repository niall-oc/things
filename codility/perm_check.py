# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
def solution(A):
    num = len(A)
    res = num
    while num > 0:
        num -= 1
        res += num
    # Arithmetic guards against double numbers
    # Set check guards against anti sum cases
    return int((res == sum(A)) and (len(set(A)) == len(A)))

