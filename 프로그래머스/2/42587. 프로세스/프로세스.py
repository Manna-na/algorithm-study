from collections import deque
def solution(priorities, location):
    queue = deque([])
    for index, value in enumerate(priorities):
        queue.append((index, value))
    answer = 0
    
    while len(queue) > 0 :
        max = 0    
        for i in range(len(queue)):
            if max < queue[i][1]:
                max = queue[i][1]  
        num = queue.popleft()
        if num[1] >= max:
            answer += 1
            max = num[1]
            if num[0] == location:
                break
        else:
            queue.append(num)
    return answer