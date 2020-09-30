# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/

def get_divisors(n):
    froot = int(n**.5)
    divs = set()
    # reverse through possible divisors which are lower than root(n)
    while froot > 0:
        if not n%froot:
            divs.add(froot)
            divs.add(n//froot) # Catch the higher diviser on the other side of froot
        froot-=1
    return divs

def solution(A):
    N = len(A)
    int_count = {}
    
    # O(N) scan to count number frequency
    for i in range(N):
        int_count[A[i]] = int_count.get(A[i], 0) + 1
    
    # Create an array for every i's non-divisor count
    div_count = {}
    
    for i, freq in int_count.items():
        divs = get_divisors(i)
        num_divs = 0
        for d in divs:
            num_divs += int_count.get(d, 0)
        div_count[i] = N-num_divs # N -  divisors = non-divisors :-)
        
    return [div_count[A[i]] for i in range(N)]