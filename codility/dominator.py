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

