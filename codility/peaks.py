# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
# 72% solution
import time

def get_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def solution(A):
    # determine N the lenght of the array
    N = len(A)
    if N<3:
        return 0 # no peaks in this case
    
    # scan the array to count the increasing slope of peaks.
    scan = [0]* N
    for i in range(1, N-1):
        if A[i] > max(A[i-1], A[i+1]):
            scan[i] = scan[i-1] + 1
        else:
            scan[i] = scan[i-1]
    scan[-1] = scan[-2] # tag last
    
    if scan[0] == scan[-1]: # if no peaks occur then exit
        return 0
    
    # determine the divisors of len(A)
    h_div = int(N**.5)

    # The union of all divisors is created and sorted. Starting with the smallest divisor 
    # divides into the max even parts first in order to find a solution quickest.
    divisors = sorted({N} | { i for i in range(h_div, 1, -1) if not N%h_div } | { N//i for i in range(h_div, 1, -1) if not N%h_div })

    # print(N, divisors, scan)
    for d in divisors: # Begin the search
        # get the start and end peak count from each chunk
        chunks = tuple(get_chunks(scan, d))
        result = len(chunks)
        # print(result, chunks)
        # for all chunks if either a peak occurs within the cunk OR the begining of the chunk is a peak!
        peaks = [(chunks[i][-1]-chunks[i][0]) or chunks[i][0] > chunks[max(i-1,0)][-1] for i in range(result)]
        
        if all(peaks): # if every chunk has a peak and this is the most chunks we can break the Array into!
            # print(chunks, peaks)
            return result
    return 0

if __name__ == '__main__':
    tests = (
        (1, ([0,1,0,1,0],)),
        (2, ([0,1,0,1,0,0],)),
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