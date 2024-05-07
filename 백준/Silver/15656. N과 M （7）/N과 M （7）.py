import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()
selected = [0] * m

def recur(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(n):
        selected[cur] = ls[i]
        recur(cur+1)

recur(0)