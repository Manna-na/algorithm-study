def solution(n):
    answer = 0
    list_s = []
    while True:
        if n < 1:
            break
        list_s.append(n % 3)
        n //= 3
    for i in range(len(list_s)):
        answer = answer + (3**(len(list_s)-i-1))*list_s[i]
    return answer


# def solution(n):
#     answer = []
#     while True:
#         if n < 3:
#             answer.append(n)
#             break
#         answer.append(n % 3)
#         n = n // 3
#     answer.reverse()
#     sum = 0
#     for i in range(len(answer)):
#         sum += (answer[i] * (3 ** i))
#     return sum
