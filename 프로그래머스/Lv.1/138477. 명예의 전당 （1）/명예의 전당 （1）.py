def solution(k, score):
    answer = []
    for i in range(len(score)):
        list_score = score[:i+1]
        list_score.sort()
        if i < k:
            answer.append(min(list_score))
        else:
            answer.append(list_score[i+1-k])
        
    return answer