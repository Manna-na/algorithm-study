from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
     # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dist = [[-1] * m for _ in range(n)]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        dist[x][y] = 1 # 시작 위치 
        
        while queue:
            nx, ny = queue.popleft()
            for k in range(4):
                rr, cc = dx[k] + nx, dy[k] + ny
                if 0<=rr<n and 0<=cc<m and dist[rr][cc] == -1 and maps[rr][cc] == 1:
                    queue.append([rr, cc])
                    dist[rr][cc] = dist[nx][ny] + 1 # 거리 갱신
                    
    bfs(0, 0)
    return dist[n-1][m-1]