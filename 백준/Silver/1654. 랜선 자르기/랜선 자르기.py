import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

start, end = 1, max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    count = sum(a//mid for a in array)
    if count >= n:
        start = mid + 1
        result = mid
    elif count < n:
        end = mid - 1
print(result)
