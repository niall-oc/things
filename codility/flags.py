# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
import time

def solution(A):
    n = len(A)
    peaks = [i for i in range(1, n-1) if A[i] > A[i-1] and A[i] > A[i+1]]
    
    num_peaks = len(peaks)
    if num_peaks < 3:
        return num_peaks # with less than 3 peaks all flags can be placed
    
    max_flags  = int((peaks[-1]-peaks[0])**.5) # Cover the case of packed flags by adding 2
    
    # limit to trying optimal attempts, don't waste cycles trying 3,4,... etc if the most will be likely 300 flags
    flag_attempts = range(max_flags+1, 0, -1)
    # print(n, max_flags, num_peaks)
    most_flags = 0
    for attempt in flag_attempts: # we are limited from 3 to max flags or num peaks
        print(attempt)
        flag_count = 1 # place flag at first peak
        next_flag = peaks[0] + attempt # reset the position of the next_flag for this attempt
        for p in peaks:
            # print(next_flag, p)
            if next_flag <= p: # it is possible to set a flag
                flag_count += 1
                next_flag = p + attempt # the next flag can go here
            if flag_count >= attempt: # when you run out of flags
                break

        if flag_count >= most_flags:
            most_flags = flag_count
        else:
            return most_flags # Stop when the solution starts to deteriorate!
    return most_flags

if __name__ == '__main__':
    tests = (
        (1, ([0,0,1,0,0],)),
        (4, ([0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0],)),
        (9, ([0]+[1,0]*36+[0]*30+[1,0],)),
        (632, ([0]+[1,0]*200000+[0],)),
    )
    for expected, args in tests:
        tic = time.perf_counter()
        res = solution(*args)
        toc = time.perf_counter()
        print(f'ARGS produced {res} in {toc - tic:0.8f} seconds')
        try:
            assert(expected == res)
        except AssertionError as e:
            print(f'ERROR {args} produced {res} when {expected} was expected!')