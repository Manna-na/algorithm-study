def solution(ingredient):
    answer = 0
    start = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1     
    return answer