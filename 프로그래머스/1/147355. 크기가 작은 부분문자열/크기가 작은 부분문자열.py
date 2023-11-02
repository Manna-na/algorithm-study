def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        test = ''
        for j in range(i, i+len(p)):
            test += t[j]
        if int(test) <= int(p):
            answer += 1
    return answer