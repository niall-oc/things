# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
# 72% solution
def get_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def solution(A):
    # determine N the lenght of the array
    N = len(A)
    if N<3:
        return 0
    
    # scan the array to count the increasing slope of peaks.
    scan = [0]* N
    for i in range(1, N-1):
        if A[i] > max(A[i-1], A[i+1]):
            scan[i] = scan[i-1] + 1
        else:
            scan[i] = scan[i-1]
    scan[-1] = scan[-2] # tag last
    
    if scan[0] == scan[-1]: #no peaks
        return 0
    
    # determine the divisors of len(A)
    h_div = int(N**.5)
    divisors = set()
    while h_div > 1:  # one block is a given and N blocks cannot all contain peaks
        if not N%h_div:
            divisors.add(h_div)
            divisors.add(N//h_div)
        h_div -= 1
    divisors.add(N)
    divisors = sorted(list(divisors), reverse=True)

    # print(N, divisors, scan)
    i = 0
    result = 0
    while i < len(divisors):

        chunks = [c[-1]-c[0] for c in get_chunks(scan, divisors[i])]
        # print(chunks)
        if all(chunks): # if a chunk dont have a peak then break the loop
            result = len(chunks)
        else:
            break
        i+=1
    return result

if __name__ == '__main__':
    print(solution([1,3,2,1]))