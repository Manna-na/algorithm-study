# 1. 괄호 문자열을 회전시키기
# 2. 괄호 문자열 올바른지 확인
# 3. 1, 2단계 반복

def solution(s):
    answer = 0
    for i in range(len(s)):
        s_rotate = s[i:]+s[:i]
        s_stack = []
        isFlag = True
        for bracket in s_rotate:
            if bracket in '[({':
                s_stack.append(bracket)
            else:
                if not s_stack: # 닫는 괄호가 나왔는데 s_stack에 아무것도 없으면 통과
                    isFlag = False
                    break
                if bracket == "]":
                    if s_stack and s_stack[-1] == "[":
                        s_stack.pop()
                elif bracket == ")":
                     if s_stack and s_stack[-1] == "(":
                        s_stack.pop()
                elif bracket == "}":
                    if s_stack and s_stack[-1] == "{":
                        s_stack.pop()
        if isFlag and not s_stack:
            answer += 1
                
    return answer