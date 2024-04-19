import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
# 슬라이딩 윈도우
start, end = 0,0
while end < n:
    curr_sum = sum(array[start:end+1])
    if curr_sum == m:
        ans += 1
        start += 1
        end += 1
    elif curr_sum > m:
        start += 1
    else:
        end += 1

print(ans)