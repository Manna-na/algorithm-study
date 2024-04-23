import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())

sheep, goat = 0, 0
ans = 0
for i in range(1, n):
    res = w-a*i-b*(n-i)
    if res == 0:
        sheep = i
        goat = n - i
        ans += 1


if ans == 1: print(sheep, goat)
else: print(-1)