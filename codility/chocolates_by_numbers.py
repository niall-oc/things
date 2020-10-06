# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

def division_sol(n, m):
    mod = n%m
    division = n//m
    start = end = m
    #print(n,m, mod, division, start, end)
    while mod:
        start = m - mod
        end = n - start
        mod = end%m
        division += (end//m) + 1
        #print(n,m, mod, division, start, end)
    return division

def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def solution(n, m):
    return n // gcd_division(n, m)