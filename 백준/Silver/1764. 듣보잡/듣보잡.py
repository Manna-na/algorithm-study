import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hearing = set()
for _ in range(n):
    hearing.add(input().strip())
ans = []
for _ in range(m):
    now = input().strip()
    if now in hearing:
        ans.append(now)
print(len(ans))
ans.sort()
for a in ans:
    print(a)