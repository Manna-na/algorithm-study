def solution(n, lost, reserve):
    list = [0]*(n+2)
    for i in reserve:
        if i not in lost:
            list[i] += 1
    new_lost = []
    for i in lost:
        if i not in reserve:
            new_lost.append(i)
    answer = n   
    new_lost.sort()
    for l in new_lost:
        print(l)
        if list[l-1] == 1:
            list[l-1] -= 1
        elif list[l+1] == 1:
            list[l+1] -= 1
        elif list[l-1] == list[l+1] == 0:
            answer -= 1
    return answer