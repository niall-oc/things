# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
def solution(A):
    # n(n+1) /2 == sum(n)
    total = sum(A)
    n = len(A) + 1 #We know one number is missing!
    expected = int((n*(n+1))/2)
    return expected - total

