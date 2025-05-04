# 1. 괄호 문자열을 회전시키기
# 2. 괄호 문자열 올바른지 확인
# 3. 1, 2단계 반복
# 0: 0-6
# 1: 1-5 5-6 0-1
def solution(s):
    answer = 0
    for i in range(len(s)):
        str = s[i:]+s[0:i]
        stack = []
        for j in range(len(str)):
            if str[j] in "[({":
                stack.append(str[j])
            elif str[j] == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(str[j])    
            elif str[j] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(str[j])
            elif str[j] == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(str[j])
        if len(stack) == 0:
            answer += 1               
    return answer