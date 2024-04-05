import sys
input = sys.stdin.readline

n = int(input())
level = [int(input()) for _ in range(n)]
now = level[-1]
result = 0
for l in level[-2::-1]:
    if now <= l:
        result += l-now+1
        now -= 1
    else:
        now = l
print(result)