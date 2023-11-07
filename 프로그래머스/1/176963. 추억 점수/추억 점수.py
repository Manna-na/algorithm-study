def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    for j in range(len(photo)):
        for k in range(len(photo[j])):
            if photo[j][k] in name:
                answer[j] += yearning[name.index(photo[j][k])]
        
    return answer