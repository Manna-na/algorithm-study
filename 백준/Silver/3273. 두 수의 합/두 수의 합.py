import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))
x = int(input())
ans = 0
s, e = 0, n-1
while s<e:
    if ls[s] + ls[e] == x:
        ans += 1
        s += 1
        e -= 1
    elif ls[s] + ls[e] > x:
        e -= 1
    elif ls[s] + ls[e] < x:
        s += 1
print(ans)