# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
#  a 60% solution I'll fix it later
def get_peaks(A):
    # first find all peaks where A[p] is greater than Ap-1] and A[p+1]
    peak_indexes = [0] * 
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak_indexes.append(i)
    return peak_indexes

def solution(A):
    peaks = get_peaks(A)
    num_peaks = len(peaks)
    if num_peaks < 3:
        return num_peaks # with less than 3 peaks all flags can be placed
    
    # if the spread is 10 then the max flags that could be placed is 3
    spread = (peaks[-1] - peaks[0])
    base = int(spread**.5) # min flags or peaks
    max_flags = base+1 if base * (base+1) <= spread else base
    
    # print("Spread: %d - Flags: %d - %s "%(spread, max_flags, peaks))
    
    flag_count = i = 0 # assume flag at pos one
    next_flag = peaks[0]
    while i < num_peaks and flag_count <= max_flags:
        # Keep checking the next index to see if a flag can be
        # print("next peak: %d, %d" % (next_flag, peaks[i]))
        if next_flag <= peaks[i]:
            flag_count+=1
            next_flag = peaks[i]+max_flags
        # print("flags: %d, next: %d"% (flag_count, next_flag))
        i+=1
    return flag_count

