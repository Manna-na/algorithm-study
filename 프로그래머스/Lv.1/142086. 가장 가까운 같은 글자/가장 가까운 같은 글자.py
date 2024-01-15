def solution(s):
    answer = []
    find_val = {}
    for i, val in enumerate(s):
        if val in find_val:
            answer.append(i-find_val[val])
        else:
            answer.append(-1)
        find_val[val] = i
    return answer

