# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
def solution(X, Y, D):
    distance = (Y-X)
    hops = distance // D
    if distance%D:
        hops += 1
    return hops

