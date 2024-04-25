import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()
ans = 0
max_val = 100 ** 3
for i in range(1, max_val):
    cnt = 0
    for n in nums:
        if i % n == 0:
            cnt += 1
    if cnt >= 3:
        ans = i
        break
print(ans)