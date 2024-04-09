import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
sum_array = [array[0]]
for i in range(1, len(array)):
    sum_array.append(array[i]+sum_array[i-1])
m = int(input())

for _ in range(m):
     a, b = map(int, input().split())
     start, end = a-2, b-1
     if start >= 0 and end-start > 0:
         print(sum_array[end]-sum_array[start])
     elif start < 0 and end-start > 0:
         print(sum_array[end])
     elif end-start == 0:
         print(sum_array[start])