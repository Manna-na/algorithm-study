import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

for t in range(T):
    m, n, k = map(int, input().split())
    maps = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    answer = 0
    # 상 하 좌 우
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[False] * n for _ in range(m)]
    def dfs(x, y):
        visited[x][y] = True # 방문해
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 배주 흰 지렁이 있는데 아직 방문안했어?
            if 0 <= nx < m and 0<= ny < n and not visited[nx][ny] and maps[nx][ny] == 1:
                # 방문해
                dfs(nx, ny)
    for r in range(m):
        for c in range(n):
            if not visited[r][c] and maps[r][c] == 1:
                dfs(r, c)
                answer += 1
    print(answer)