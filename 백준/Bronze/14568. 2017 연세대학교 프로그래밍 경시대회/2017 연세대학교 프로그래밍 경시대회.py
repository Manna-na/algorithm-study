import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(1, n): # 영훈이
    for j in range(i+2, n):
        for k in range(2, n, 2): # 택희
            now_candy = i + j +k
            if now_candy == n:
                ans += 1
print(ans)