def solution(s):
    answer = True
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_s = list(s)
    cnt = 0
    for i in list_s:
        if i not in numbers:
            answer = False
        else:
           cnt += 1
    if cnt < 4 or cnt == 5 or cnt > 6:
        answer = False
    return answer