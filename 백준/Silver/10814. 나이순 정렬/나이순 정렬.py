import sys
input = sys.stdin.readline

n = int(input())
list = [input().split() for _ in range(n)]
list.sort(key=lambda x:int(x[0]))
for i in range(n):
    print(list[i][0], list[i][1])
