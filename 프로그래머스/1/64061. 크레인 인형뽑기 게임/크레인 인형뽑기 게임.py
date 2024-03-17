# O(N^2)
# 1. move열에 해당하는 board 값 중 0이 아닌 값을 찾아서 stack에 넣기
# 1-1. 모든 값이 0이면 pass
# 2. stack의 top과 board의 값이 같으면 터트리기 +2

def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for j in range(len(board[0])):
            if board[j][m-1] > 0:
                if stack and stack[-1] == board[j][m-1]:
                    answer += 2
                    stack.pop()
                elif stack and stack[-1] != board[j][m-1]:
                    stack.append(board[j][m-1])
                else:
                    stack.append(board[j][m-1])
                board[j][m-1] = 0
                break
    return answer