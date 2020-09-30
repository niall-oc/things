# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
def solution(S, P, Q):
    # write your code in Python 3.6
    A=0; C=1; G=2 # indexes for occurences
    
    # greate an array to trak the occurance of character
    occurence = [
        [0] * (len(S)+1),
        [0] * (len(S)+1),
        [0] * (len(S)+1)
    ]
    idx = 0
    # fill occurence
    while idx < len(S):
        occurence[A][idx+1] = occurence[A][idx] + (S[idx] == 'A') # boolean 1 or 0
        occurence[C][idx+1] = occurence[C][idx] + (S[idx] == 'C') # boolean 1 or 0
        occurence[G][idx+1] = occurence[G][idx] + (S[idx] == 'G') # boolean 1 or 0
        idx += 1
    
    results = []
    idx=0
    while idx < len(P):
        start = P[idx]
        end = Q[idx] + 1
        if occurence[A][end] - occurence[A][start]: # If numbers are not identical an A occured
            results.append(1) # Weight of an A
        elif occurence[C][end] - occurence[C][start]: # If numbers are not identical an C occured
            results.append(2) # Weight of an C
        elif occurence[G][end] - occurence[G][start]: # If numbers are not identical an G occured
            results.append(3) # Weight of an G
        else:
            results.append(4) # weight of a T
        idx += 1
    return results

