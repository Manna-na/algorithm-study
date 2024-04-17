import sys
input = sys.stdin.readline

# 정렬해서 그냥 차이가 가장 작은거 골라
n = int(input())
array = list(map(int, input().split()))
array.sort()
if n%2 == 0:
    print(array[n//2-1])
else:
    print(array[n//2])