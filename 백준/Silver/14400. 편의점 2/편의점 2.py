import sys
input = sys.stdin.readline

n = int(input())
dist_x = [0] * n
dist_y = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    dist_x[i] = x
    dist_y[i] = y

dist_y.sort()
dist_x.sort()
ans = 0
for i in range(n):
    if n%2 == 0:
        ans += abs(dist_x[n//2]-dist_x[i]) + abs(dist_y[n//2]-dist_y[i])
    else:
        ans += abs(dist_x[(n-1)//2]-dist_x[i]) + abs(dist_y[(n-1)//2]-dist_y[i])

print(ans)