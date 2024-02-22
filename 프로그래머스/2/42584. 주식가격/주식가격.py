def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for p in range(1, len(prices)):
        while stack and prices[p] < prices[stack[-1]]:
            s_idx = stack.pop()
            answer[s_idx] = p-s_idx
        stack.append(p)
    while stack:
        s_idx = stack.pop()
        answer[s_idx] = len(prices)-s_idx-1
    return answer