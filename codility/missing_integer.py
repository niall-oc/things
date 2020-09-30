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

