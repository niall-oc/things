def factorial(n):
    # recursive
    if not n:
        return 1
    else:
        return n * factorial(n-1)

def factorial_for(n):
    if not n:
        return 1
    else:
        r = 1
        for i in range(1, n+1):
            r = i*r
        return r

def factorial_while(n):
    if not n:
        return 1
    else:
        i = r = 1
        while i < n+1:
            r = i*r
            i += 1
        return r

def fibonacci(n):
    # recursive
    if not n:
        return 0
    elif n<3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_itr(n, seq=False):
    # iterator
    if not n:
        r = [0]
    elif n<3:
        r =  [0,1,1] if n == 2 else [0,1]
    else:
        r = [0,1,1]
        for _ in range(3, n+1):
            r += [r[-2] + r[-1]]
    
    return r if seq else r[-1]

