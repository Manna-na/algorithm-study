import sys

N = int(input())
A = [0] * N # 수열의 현재 값 배열
for i in range(N):
    A[i] = int(sys.stdin.readline().strip())

stack = []
num = 1 # 스택에 푸시해야 할 숫자
result = True
answer = ""

for i in range(N):
    if A[i] >= num:
        # 수열이 오름차순 수보다 크거나 같을때
        while A[i] >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"

    else:
        # 수열이 오름차순 수보다 작을떄
        # 스택이 비어있거나 스택에 푸시해야할 숫자가 수열 값보다 작을때
        if not stack or stack.pop() < A[i]:
            result = False
            break
        answer += "-\n"

if result:
    print(answer)
else:
    print("NO")