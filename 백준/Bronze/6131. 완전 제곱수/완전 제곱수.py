import sys
input = sys.stdin.readline

n = int(input())
ans = 0
# 시간복잡도 : O(n^2)까지 가능할거야 500 * 500 이면 250000, 
# 1초에 1억번, 100000000
for a in range(1, 501):
    for b in range(1, 501):
        if a**2 == b**2 + n:
            ans += 1

print(ans)