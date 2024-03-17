    
def solution(s):
    answer = 0
    arr = list(s)
    for i in range(len(s)):
        stack = []
        arr = s[i:len(s)]+s[0:i]
        for j in arr:
            if j == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(j)
            elif j == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(j)
            elif j == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(j)
            else:
                stack.append(j)
        if len(stack) == 0:
            answer += 1
            
    return answer