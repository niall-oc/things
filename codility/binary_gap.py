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

