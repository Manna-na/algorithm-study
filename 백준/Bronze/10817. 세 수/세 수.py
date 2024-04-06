import sys
input = sys.stdin.readline


array = list(map(int, input().split()))
array.sort()
print(array[1])