def solution(n):
    answer = ''
    list_num = []
    while n > 0:
        list_num.append(n%10)
        n//=10
    list_num.sort(reverse=True)
    for i in list_num:
        answer += str(i)
    answer = int(answer)
    
    return answer