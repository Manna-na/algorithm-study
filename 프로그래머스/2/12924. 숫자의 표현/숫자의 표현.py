def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_val = 0
        while sum_val < n:
            sum_val += i
            i+=1
        if sum_val == n:
            answer+= 1
    return answer