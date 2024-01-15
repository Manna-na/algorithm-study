def solution(s):
    answer = ''
    arr = list(s.split(" "))
    for arr_val in arr:
        for index, value in enumerate(arr_val):
            if index % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += " "
    return answer[:-1]