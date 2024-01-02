import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
array = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    u, v = map(int ,input().split())
    array[u].append(v)
    array[v].append(u)

def dfs(node):
    visited[node] = True
    for i in array[node]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
