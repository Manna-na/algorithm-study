def solution(k, tangerine):
    memo = [0 for _ in range(max(tangerine)+1)]
    for t in tangerine:
        memo[t] += 1
    memo.sort(reverse=True)
    answer = 0
    sum = 0    
    for i in range(len(memo)):
        if sum >= k:
            break
        sum += memo[i]
        answer += 1
    return answer