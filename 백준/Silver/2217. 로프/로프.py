n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()

ans = []
for i in rope:
    ans.append(i*n)
    n -= 1

print(max(ans))