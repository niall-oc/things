# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

def solution(A):
    # Given 100 integers the first 101 positive integers has at least 1 value missing.
    n = len(A)
    MAX = n+1
    possible_answers = [0] * MAX
    
    for value in A:
        # if its positive and in range
        if 1 <= value <= MAX:
            # insert a value at the correct index
            possible_answers[value-1] = value
    
    # the first missing index encountered is the lowest int 1
    for index in range(MAX):
        if possible_answers[index] == 0:
            return index + 1
            
    return 1

def solution_other(A):
    n = len(A)
    A.sort()
    
    if A[-1] < 1:
        return 1
    
    passed_zero = False
    for i in range(n):

        if not passed_zero and A[i] > 0 :
            passed_zero = True
            if A[i] > 1:
                return 1
        elif passed_zero and A[i] - A[i-1] > 1:
            return A[i] - 1
            
    return A[-1] + 1


