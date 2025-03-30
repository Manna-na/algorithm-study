import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
array = list(map(int, input().split()))
sum_array = [0] * (n+1)

for i in range(n):
    sum_array[i+1] = sum_array[i] + array[i]

for _ in range(m):
    start, end = map(int, input().split())
    print(sum_array[end]-sum_array[start-1])
