def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        # m-1열에 위치한 인형 중 0이 아닌 수가 처음으로 나오는 곳
        now_idx = -1
        for i in range(len(board[0])):
            if board[i][m-1] > 0:
                now_idx = i
                break
        # m-1열에 모두 0만 있어? 지나가
        if now_idx == -1: continue
        else:
            if stack and stack[-1] == board[now_idx][m-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(board[now_idx][m-1])
            board[now_idx][m-1] = 0
    return answer