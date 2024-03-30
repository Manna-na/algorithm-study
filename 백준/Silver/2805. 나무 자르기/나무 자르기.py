import sys
input = sys.stdin.readline
# 시간복잡도 : 10^6 -> O(nlogn), 이분탐색
n, m = map(int, input().split())
array = list(map(int, input().split()))

# sum이 m보다 크거나 같으면 되는거네
# 1. 상한을 제일 큰 값으로 두고 하한은 1로 두기
# 2. array의 값들에서 mid를 뺸 값의 합이 m보다 크면 하한 올리기
# 3. array의 값들에서 mid 뺀 값의 합이 m이면 끝내
# 4. array의 값들에서 mid 뺀 값의 합이 m보다 작으면 상한 내리기

start, end = 0, max(array)
while start <= end:
    mid = (start+end) // 2
    now_sum = 0
    for r in array:
        if r > mid:
            now_sum += (r-mid)
    if now_sum >= m:
        start = mid+1
    elif now_sum < m:
        end = mid-1
print(end)