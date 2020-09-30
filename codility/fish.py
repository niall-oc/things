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


