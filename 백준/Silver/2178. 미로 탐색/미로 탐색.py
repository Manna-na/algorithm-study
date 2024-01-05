import sys
from collections import deque

input = sys.stdin.readline

# bfs 문제
n, m = map(int, input().split())
maze = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        maze[i][j] = int(numbers[j])

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(s, e):
    queue = deque([(s, e)])
    visited[s][e] = True
    while queue:
        vx, vy = queue.popleft()
        # 상 하 좌 우 탐색 시작
        for k in range(4):
            x = vx + dx[k]
            y = vy + dy[k]
            # 좌표 유효성 검사
            if x >= 0 and x < n and y >= 0 and y < m:
                if maze[x][y] != 0 and not visited[x][y]:
                    queue.append((x, y))
                    visited[x][y] = True
                    maze[x][y] = maze[vx][vy] + 1
bfs(0, 0)
print(maze[n-1][m-1])


