import sys
input = sys.stdin.readline

n , m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
selected = [0] * m
visited = [False] * n
def recur(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = ls[i]
        recur(cur+1)
        visited[i] = False
recur(0)