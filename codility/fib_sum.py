# discover numbers that can be made from 2 fibnocacci numbers.

def gen_fib(n):
    fn = [0,1]
    i = 2
    s = 2
    while s < n:
        s = fn[i-2] + fn[i-1]
        fn.append(s)
        i+=1
    return fn

def sum_fibs(fn):
    N = len(fn)
    permutate = { 
        fn[i] + fn[j]
        for i in range(0, N-1)
        for j in range(i+1, N) 
    }
    return permutate



def solution():
    pass

if __name__ == '__main__':
    N = 1000000
    sub_fibs = [i for i in list(sum_fibs(gen_fib(N))) if i<N]
    print(sorted(sub_fibs))
