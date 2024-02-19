def solution(board, h, w):
    answer = 0
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] #상하좌우
    for k in range(4):
        nx, ny = h + dx[k] , w + dy[k]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[h][w] == board[nx][ny]:
            answer += 1
    return answer