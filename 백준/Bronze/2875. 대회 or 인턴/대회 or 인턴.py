import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 여 남 인턴쉽
ans = 0
min_val = min(n, m)
if n < 2 or m == 0:
    print(0)
else:
    now_cnt = 0
    for i in range(1, min_val+1):
        if n-2*i >=0 and n - 2*i + m - i >= k:
            now_cnt += 1
        ans = max(now_cnt, ans)
print(ans)