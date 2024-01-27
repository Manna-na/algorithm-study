import sys
input = sys.stdin.readline

n = int(input())
memo = {}
for _ in range(n):
    num = int(input())
    for i in range(1, num+1):
        # base case
        if i == 1:
            memo[1] = 1
        elif i == 2:
            memo[2] = 2
        elif i == 3:
            memo[3] = 4
        if i > 3:
            memo[i] = memo[i-3] + memo[i-2] + memo[i-1]
    print(memo[num])