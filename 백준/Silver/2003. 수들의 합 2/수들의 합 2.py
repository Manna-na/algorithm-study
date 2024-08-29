import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

s = 0
now = 0
ans = 0

for e in range(n):
    now += ls[e]

    while now > m:
        now -= ls[s]
        s += 1

    if now == m:
        ans += 1

print(ans)