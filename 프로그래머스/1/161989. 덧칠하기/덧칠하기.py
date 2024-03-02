def solution(n, m, section):
    answer = 0
    start = 0
    
    while start < len(section):
        end = start
        while end < len(section) - 1 and section[end + 1] - section[start] < m:
            end += 1
        
        answer += 1
        start = end + 1
    
    return answer
