# 1. 스택이 비어있지 않고 현재 값과 stack의 [-1] 값이 같으면 제거
# 2. 스택 비었는지 확인

def solution(s):
    # 10^6 -> O(NlogN)
    s_stack = []
    for i in s:
        if s_stack and s_stack[-1] == i:
            s_stack.pop()
        else:
            s_stack.append(i)
    if s_stack:
        return 0
    else:
        return 1
    