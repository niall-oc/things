'''
Solutions to codility lessons.
Each solution achives an over all score of 100%
'''

# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    bits = "{0:b}".format(N)
    count = 0
    max = 0
    open = False
    for b in bits:
        # requires a '1' to open and close
        if not open:
            if b == '0':
                open = True
                count += 1
        elif open:
            if b == '0':
                count += 1
            else:
                open = False
                if count > max:
                    max = count
                count = 0
    return max

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

# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
def solution(A):
    r = max(A)
    r_index = A.index(r)
    q = max(A[:r_index])
    q_index = A.index(q)
    p = max(A[:q_index])
    return p*q*r

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
