'''
Solutions to codility lessons.
Each solution achives an over all score of 100%
'''

# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    # write your code in Python 3.6
    gaps = []
    count = 0
    for b in "{0:b}".format(N):
        if b == '1':
            gaps.append(count)
            count = 0
        else:
            count += 1
    return max(gaps)

# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
def solution(A):
    result=0
    for item in A:
        result ^= item
    return result

# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
def solution(A):
    left = A[0]
    right = sum(A[1:])
    min_difference = abs(left - right)
    for index in range(1, len(A)-1):
        left += A[index]
        right -=A[index]
        diff = abs(left - right)
        if diff < min_difference:
            min_difference = diff
    return min_difference

# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
def solution(A):
    # n(n+1) /2 == sum(n)
    total = sum(A)
    n = len(A) + 1 #We know one number is missing!
    expected = int((n*(n+1))/2)
    return expected - total

# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
def solution(A):
    num = len(A)
    res = num
    while num > 0:
        num -= 1
        res += num
    # Arithmetic guards against double numbers
    # Set check guards against anti sum cases
    return int((res == sum(A)) and (len(set(A)) == len(A)))

# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
def solution(X, A):
    leaf_set = set()
    for index in range(0, len(A)):
        if A[index] > X:
            continue
        leaf_set.add(A[index])
        if (len(leaf_set) == X):
            return index
    return -1

# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
def solution(A):
    # Given 100 integers the first 101 positive integers has at least 1 value missing.
    possible_answers = [0] * (len(A) +1)
    
    for value in A:
        # if its positive and in range
        if 1 <= value <= len(A) + 1:
            # insert a value at the correct index
            possible_answers[value-1] = value
    
    # the first missing index encountered is the lowest int -1
    for index in range(0, len(A)+1):
        if possible_answers[index] == 0:
            return index + 1
            
    return -1

# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
def solution(N, A):
    count = [0] * N
    max_count = 0
    last_max = False
    for val in A:
        if val == N + 1 and last_max == False:
            count = [max_count] * N
            last_max = True
            continue
        if val <= N:
            count[val - 1] += 1
            max_count = max(count[val - 1], max_count)
            last_max = False
    return count


# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    l = len(A)
    if l == 3:
        return A[0] * A[1] * A[2]
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
def solution(A, K):
    N = len(A)
    if N:
        K = K%N
        if K:
            return A[-K:]+A[:N-K]
    return A

# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
def solution(X, Y, D):
    distance = (Y-X)
    hops = distance // D
    if distance%D:
        hops += 1
    return hops

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
 
    remove =  ((A + K -1) // K) * K
 
    if remove > B:
      return 0
 
    return ((B - remove) // K) + 1

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
def solution(A, B, K):
    # if A, B,K are already valid inputs!
    return ((B // K) + 1) - ((A + K -1) // K)


# https://app.codility.com/programmers/lessons/6-sorting/distinct/
def solution(A):
    return len(set(A))

# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# Detected time complexity: O(N*log(N)) or O(N)
def solution(A):
    N = len(A)
    # Sort the boundries of the discs
    indexes = range(0,N)
    upper_x = sorted([index+A[index] for index in indexes])
    lower_x = sorted([index-A[index] for index in indexes])
    
    I = 0  # intersections counted
    
    lower_index = 0
    for upper_index in indexes:
        # count only the discs that intersect
        disc = upper_x[upper_index]
        while lower_index < N and disc >= lower_x[lower_index]:
            lower_index += 1
        
        I += lower_index - upper_index -1
        if I > 10000000:
            return -1
    return I


# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
def solution(A, B):
    down_stream_stack = []
    survivor = []
    for i in range(0, len(A)):
        if B[i]:  # the direction flag is 1 or downstream
            down_stream_stack.append(A[i])
            
        elif len(down_stream_stack): # its an upstream fish that must contend with down stream swimmers
        
            while len(down_stream_stack):
                if down_stream_stack[-1] < A[i]:
                    down_stream_stack.pop()
                else:
                    break
            
            else:  #  All the downstream fish are eaten
                survivor.append(A[i])
                
        else:  # its an upstream fish and there are no previous downstream swimmers
            survivor.append(A[i])
            
    return len(survivor+down_stream_stack)


# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
def solution(S):
    stack = []
    openers, closers = '{[(', '}])'
    for char in S:
        if char in openers:
            stack.append(char)
        else:
            # if there is a mismatch or an empty stack for a closing char its a fail
            if stack:
                sc = stack.pop()
                if openers.index(sc) != closers.index(char):
                    return 0
            else:
                return 0
    if stack:  # stack should be empty
        return 0
    return 1

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

# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
def solution(A):
    # write your code in Python 3.6
    prefix_sum = [0] * len(A)
    avg = (A[0] + A[1]) / 2
    min_idx = 0
    
    idx = 2
    while idx < len(A):
        cur = (A[idx-2] + A[idx-1] + A[idx]) / 3
        if cur < avg :
            avg = cur
            min_idx = idx-2
        
        cur = (A[idx-1] + A[idx]) / 2
        if cur < avg :
            avg = cur
            min_idx = idx-1
        idx += 1
    
    return min_idx

# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/start/
def solution(A):
    # write your code in Python 3.6
    MAX = 1000000000
    weight = sum(A)

    i = 0
    passes = 0
    while i < len(A) and weight:
        if not A[i]: # a 0 encountered
            passes += weight
        else:
            weight -= 1
        
        if passes > MAX:
            return -1
        i+=1
    
    return passes

# https://app.codility.com/programmers/lessons/6-sorting/triangle/
def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    i = 2
    if N > i:
        while i < N:
            if A[i-2] + A[i-1] > A[i]:
                return 1
            i+=1
    return 0

# https://app.codility.com/programmers/lessons/8-leader/dominator/
def solution(A):
    # write your code in Python 3.6
    candidate = []
    index = []
    for i in range(len(A)):
        if not candidate or A[i] == candidate[-1]:
            candidate.append(A[i])
            index.append(i)
        else:
            candidate.pop()
            index.pop()
    if candidate:
        count = sum([1 for i in A if i == candidate[0]])
        return index[0] if count > len(A) // 2 else -1
    return -1

# https://app.codility.com/programmers/lessons/8-leader/equi_leader/
def solution(A):
    # write your code in Python 3.6
    candidate = []
    index = []
    N = len(A)
    # print('A contains %s elements'%N)
    indexes = range(N)
    for i in indexes:
        if not candidate or A[i] == candidate[-1]:
            candidate.append(A[i])
            index.append(i)
        else:
            candidate.pop()
            index.pop()
    
    if candidate: # there is a candidate
        c_indexes = [int(i==candidate[0]) for i in A] # candidate indexes
        candidate_total = sum(c_indexes) 
        
        if candidate_total > N // 2: # candidate is leader
        
            equi_leader_count = 0
            candidate_count = 0
            for i in indexes:
                if c_indexes[i]: # leader found
                    candidate_count += 1
                # leader on both left and right
                equi_split = (candidate_count > (i+1) // 2) and ((candidate_total - candidate_count) > (N-(i+1)) // 2)
                # print(candidate_count, '>', (i+1)//2, ' | ', candidate_total - candidate_count, '>', (N-(i+1))//2, equi_split)
                if equi_split:
                    equi_leader_count += 1
            return equi_leader_count
    return 0

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
def solution(A):
    n = len(A)
    max_starts = [0]*n
    max_ends = [0]*n
    
    max_sum = 0
    for i in range(n-2, 0, -1):          
        max_sum = max(0, max_sum+A[i])
        max_ends[i] = max_sum
    
    max_sum = 0
    for i in range(1, n-1):          
        max_sum = max(0, max_sum+A[i])
        max_starts[i] = max_sum
    
    max_sum = 0
    for i in range(0, n-2):
        max_sum = max(max_sum, max_starts[i] + max_ends[i+2])

    return max_sum;

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
def max_slice_prof(A, start, end):
    ending = 0
    max_slice = 0
    for i in range(start, end):
        ending = max(0, ending + A[i])
        max_slice = max(max_slice, ending)
    return max_slice

def solution(A):
    n = len(A)
    moves =[0]*n
    
    for i in range(1, n):
        moves[i] = A[i] - A[i-1]
    return max_slice_prof(moves, 0, n)

# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
def solution(A):
    base = min(A)
    ending = 0
    max_slice = base
    for a in A:
        ending = max(base, ending + a, a)
        max_slice = max(max_slice, ending)
    return max_slice

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
def solution(N):
    # write your code in Python 3.6
    R = int(N**.5)
    result = 0
    
    for i in range(1, R+1):
        if not N%i:
            result = result + 2
    
    if R*R == N:
        result = result - 1
        
    return result


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

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
def solution(N):
    # write your code in Python 3.6
    max_int_root = int(N**.5)
    
    # is it a square?
    if max_int_root**2 == N:
        return 4*max_int_root
    
    while N%max_int_root:
        max_int_root -= 1 # find the next highest commond divisor.
        
    B = N//max_int_root

    return 2 * (B+max_int_root)

# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
# 40% solution
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
    
    divisors = sorted(list(divisors), reverse=True)

    # print(N, divisors)
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