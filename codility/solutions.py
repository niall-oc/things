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

#https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
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

#https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/start/
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

#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
def max_slice(A, start, end):
    ending = 0
    max_slice = 0
    for i in range(start, end):
        ending = max(0, ending + A[i])
        max_slice = max(max_slice, ending)
    #print(A, A[start:end], start, end, '--', max_slice)
    return max_slice

def solution(A):
    n=len(A)
    max_double_slice = 0
    #Split the list at every valid midpoint and calculate the max slice on each side.
    for i in range(1, n-1):
        left = max_slice(A, 1, i)
        right = max_slice(A, i+1, n-1)
        #print("1:%d = %d -- %d:%d = %d"%(i-1, left, i+1, n-1, right))
        max_double_slice = max(max_double_slice, left+right)
        #print(max_double_slice, '\n')
    return max_double_slice
