def solution(n):
    answer = ''
    str_arr = ['수', '박']
    for i in range(n):
        if i % 2 == 1:
            answer += str_arr[1]
        else:
            answer += str_arr[0]
    return answer