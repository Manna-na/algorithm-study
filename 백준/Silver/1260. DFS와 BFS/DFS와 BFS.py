import sys
from collections import deque
sys.setrecursionlimit(10000)
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()
def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

dfs(v)
print()
visited = [False] * (n+1)

def bfs(node):
    queue = deque([node])
    visited[node] = True
    # queue가 빌때까지 해야하니까
    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(v)