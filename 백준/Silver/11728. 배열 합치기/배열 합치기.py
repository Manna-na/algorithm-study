import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))
plus = a_array+b_array
plus.sort()
print(*plus)