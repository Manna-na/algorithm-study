import sys
input = sys.stdin.readline

n, m = map(int, input().split())
selected = [0] * m
def recur(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(n):
        selected[cur] = i+1
        recur(cur+1)

recur(0)