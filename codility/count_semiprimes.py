# https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_semiprimes/
# 77% solution 2 perf tests very close

def get_sieve(n):
    # Use the sieve or eratosthenes to produce an array of primes
    factors = [0] * (n+1)
    i=2
    i2 = i*i
    while (i2 <= n):
        if not factors[i]:
            k = i2
            while k <= n:
                if not factors[k]:
                    factors[k] = i
                k += i
        i += 1
        i2 = i*i
    return factors

def is_semi_prime(n, factors):
    if factors[n]: # Check its not a prime
        for r in range(int(n**.5)+1, 1, -1):
            if not n%r:
                d = n//r
                return (not factors[d]) and (not factors[r])
    return False

def solution(N, P, Q):
    # produce a slope of increasing semi primes
    factors = get_sieve(N)
    slope = [0] * (N+1)
    for i in range(1, N+1):
        slope[i] = slope[i-1] + is_semi_prime(i, factors) # Auto casting!! :-)
    # Optimus Prime!
    print(list(enumerate(slope)))
    return [slope[Q[j]] - slope[P[j]-1] for j in range(len(P))]


if __name__ == '__main__':
    test_cases = (
        ( [10,4,0, 10, 11], (33, [1, 4, 16, 4, 1], [26, 10, 20, 28, 33]), ),
    )
    for expected, args in test_cases:
        got = solution(*args)
        print(expected, got)
        assert(expected == got)