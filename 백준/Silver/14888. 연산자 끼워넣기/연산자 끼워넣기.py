import sys
input = sys.stdin.readline

# +, -, *, /
# 완탐 해보자, 연산자를 순열로 구해볼까

n = int(input())
nums = list(map(int, input().split()))
ope = list(map(int, input().split()))
operator = []

for o in range(4):
    if o == 0:
        for i in range(ope[0]):
            operator.append('+')
    elif o == 1:
        for i in range(ope[1]):
            operator.append('-')
    elif o == 2:
        for i in range(ope[2]):
            operator.append('*')
    else:
        for i in range(ope[3]):
            operator.append('/')

selected = [0] * len(operator)
visited = [False] * len(operator)
last_used = ''
max_ans = -sys.maxsize
min_ans = sys.maxsize
def recur(cur):
    global last_used, max_ans, min_ans
    if cur == len(operator):
        # print(*selected)
        # 합 구하기
        ans = operate(selected)
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
        # print()
        return
    for i in range(len(operator)):
        if visited[i]:
            continue
        selected[cur] = operator[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False # 초기화
        last_used = operator[i]


def operate(selected):
    global nums
    ans = nums[0]
    for i in range(len(selected)):
        if selected[i] == '+':
            ans += nums[i+1]
        elif selected[i] == '-':
            ans -= nums[i+1]
        elif selected[i] == '/':
            if ans * nums[i+1] > 0:
                ans //= nums[i+1]
            else:
                ans = (abs(ans) // abs(nums[i + 1])) * (-1)
        else:
            ans *= nums[i+1]

    return ans
recur(0)
print(max_ans)
print(min_ans)