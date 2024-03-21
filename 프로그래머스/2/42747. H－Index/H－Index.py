def solution(citations):
    answer = 0
    citations.sort()
    for c in range(len(citations)):
        min_ans = min(citations[c], len(citations)-c)
        answer = max(min_ans, answer)
    return answer