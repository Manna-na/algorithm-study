# 1단계 : 좌표평면 벗어나는지 체크
# 2단계 : 명령어를 통해 다음 좌표 결정
# 3단계 : 겹치는 좌표 중복 처리
# 4단계 : 주어진 명령어로 움직이면서 좌표 저장
# 5단계 : 벗어난 좌표는 인정 no
# 6단계 : A->B인 경우 B->A도 추가해야함 **

def solution(dirs):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = 5, 5
    dirc = set()
    for dir in dirs:
        if dir=='U':
            nx, ny = x+dx[0], y+dy[0]
        elif dir == 'D':
            nx, ny = x+dx[1], y+dy[1]
        elif dir == 'R':
            nx, ny = x+dx[2], y+dy[2]
        else:
            nx, ny = x+dx[3], y+dy[3]
        if 0<=nx<=10 and 0<=ny<=10:
            dirc.add((x, y, nx, ny))
            dirc.add((nx, ny, x, y))
            x, y = nx, ny

    return len(dirc) // 2

# print(solution("ULURRDLLU")) #7
# print(solution("LULLLLLLU")) #7