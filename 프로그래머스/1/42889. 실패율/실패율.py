def solution(N, stages):
    answer = []
    dict = {}
    total = len(stages)
    for i in range(1, N+1):
        fail = stages.count(i)
        if total == 0:
            dict[i] = 0
        else:
            dict[i] = fail/total
        total -= fail

    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    print(sorted_dict)
    for i in sorted_dict:
        answer.append(i[0])
    print(answer)
    return answer