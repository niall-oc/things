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

