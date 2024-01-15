def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    index = 0
    for _ in range(len(score)//m):
        arr = score[index:index+m]
        answer += min(arr) * m
        index += m
    return answer