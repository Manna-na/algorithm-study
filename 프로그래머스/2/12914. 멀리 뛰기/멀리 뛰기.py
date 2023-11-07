def solution(n):
    d = [0 for _ in range(2001)]
    answer = 0
    d[1] = 1
    d[2] = 2
    if n >= 3:
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
    answer = d[n] % 1234567
    return answer
