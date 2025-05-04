# 1. 스택이 비어있지 않고 현재 값과 stack의 [-1] 값이 같으면 제거
# 2. 스택 비었는지 확인

def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return 1 if not stack else 0
    