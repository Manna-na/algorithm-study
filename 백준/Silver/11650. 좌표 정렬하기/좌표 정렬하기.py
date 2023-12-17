import sys
input = sys.stdin.readline

n = int(input())
numbers = [input().split() for _ in range(n)]
numbers.sort(key=lambda x:(int(x[0]), int(x[1])))
for x, y in numbers:
    print(x, y)