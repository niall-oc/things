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

