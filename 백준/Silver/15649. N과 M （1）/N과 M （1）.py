import sys
input = sys.stdin.readline

n, m = map(int, input().split())

selected = [0] * m
visited = [False] * n
def recur(cur):
    if cur == m: # cur이 먼데? 자리 수 아냐?
        print(*selected)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        selected[cur] = i+1
        recur(cur+1)
        visited[i] = False
recur(0)