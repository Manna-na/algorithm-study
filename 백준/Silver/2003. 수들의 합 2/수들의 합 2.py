import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
ans = 0
# 슬라이딩 윈도우
start, end = 0,0
now_sum = array[start]
while end < n:
    if now_sum == m:
        ans += 1
        now_sum -= array[start] # 이전꺼 빼
        start += 1
        if end+1 >= n:
            break
        end += 1
        now_sum += array[end] # 이후꺼 더해
    elif now_sum > m:
        now_sum -= array[start]
        start += 1
    else:
        if end+1 >= n:
            break
        end += 1
        now_sum += array[end]

print(ans)