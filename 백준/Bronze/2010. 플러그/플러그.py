import sys
input = sys.stdin.readline

n = int(input())

result = 1
for i in range(n):
    con = int(input())
    result += con - 1

print(result)