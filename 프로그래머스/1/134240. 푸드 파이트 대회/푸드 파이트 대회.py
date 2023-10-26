def solution(food):
    answer = ''
    for index, num in enumerate(food):
        if num // 2  >= 1:
            answer += (str(index) * (num//2)) 
    answer += '0' + answer[::-1]
    return answer