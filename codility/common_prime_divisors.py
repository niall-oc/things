# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/

def gcd_division(a, b):
    if not a%b:
        return b
    return gcd_division(b, a%b)

def prime_reduce(n, gcd):
    na = n // gcd
    ngcd = gcd_division(na, gcd)
    if na == 1:
        return True # success base case
    elif ngcd == 1:
        return False
    return prime_reduce(na, ngcd)

def solution(A, B):
    # A sieve to cover both number ranges
    Z = len(A)
    result = 0
    for i in range(0, Z):
        a, b = A[i], B[i]
        if a == b:
            result += 1
        else:
            gcd = gcd_division(a, b)
            result += (prime_reduce(a, gcd) and prime_reduce(b, gcd))
    return result

if __name__ == '__main__':
    test_cases = (
        (1, ([15, 10, 9], [75, 30, 5]) ),
        (2, ([7, 17, 5, 3], [7, 11, 5, 2]) ),
        (2, ([3, 9, 20, 11], [9, 81, 5, 13]) ),
    )
    for expected, args in test_cases:
        got = solution(*args)
        print('result', expected, got)
        assert(expected == got)