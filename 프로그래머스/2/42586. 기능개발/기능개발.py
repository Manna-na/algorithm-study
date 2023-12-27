import math

def solution(progresses, speeds):
    answer = []
    new = []
    for p,s in zip(progresses, speeds):
        new.append(int(math.ceil((100-p)/s)))
    stack = [new[0]]
    for i in range(1, len(new)):
        if stack[0] >= new[i]:
            stack.append(new[i])
        else:
            answer.append(len(stack))  
            stack = [new[i]]
            
    answer.append(len(stack))
    return answer