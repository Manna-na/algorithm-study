def solution(numbers):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for i in numbers:
        if i in num:
            num.remove(i)
    answer = sum(num)
    return answer