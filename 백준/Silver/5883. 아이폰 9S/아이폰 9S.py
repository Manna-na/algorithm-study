import sys
input = sys.stdin.readline

n = int(input())
# 시간복잡도 O(n^2) 까지 가능해요
b = [int(input()) for _ in range(n)]
diff = set(b)
ans = 0
for d in diff:
    now_cnt = 1
    last_used = -1
    for i in range(n):
        if b[i] == d:
            continue
        if last_used == b[i]:
            now_cnt += 1
        else:
            now_cnt = 1
        ans = max(ans, now_cnt)
        last_used = b[i]

print(ans)