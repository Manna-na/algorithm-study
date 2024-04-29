import sys
input = sys.stdin.readline

n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for xx in range(x, 10+x):
        for yy in range(y, 10+y):
            array[xx][yy] += 1
ans = 0
for i in range(101):
    for j in range(101):
        if array[i][j] >= 1:
            ans += 1

print(ans)