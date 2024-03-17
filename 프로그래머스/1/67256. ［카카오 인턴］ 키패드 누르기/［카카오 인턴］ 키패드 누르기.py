# 1. 왼쪽 vs 오른쪽, 손가락 위치 갱신
# 2. 가운데 위치
# 2-1. 현재 왼손, 현재 오른손과의 위치 계산, 가까운 쪽으로
# 2-2. 위치 같으면 오른손 잡이, 왼손잡이로 판단
# 시간복잡도 O(N^2)

def solution(numbers, hand):
    answer = ''
    key_pad = [[1, 2, 3], [4, 5, 6],[7, 8, 9],['*', 0, '#']]
    now_r, now_l = [3, 0], [3, 2]
    for n in numbers:
        if n in [1, 4, 7]:
            for j in range(len(key_pad)):
                if key_pad[j][0] == n:
                    now_l = [j, 0]
                    answer += 'L'
        elif n in [3, 6, 9]:
            for j in range(len(key_pad)):
                if key_pad[j][2] == n:
                    # now_r = key_pad[j][2]
                    now_r = [j, 2]
                    answer += 'R'
        else:
            for j in range(len(key_pad)):
                if key_pad[j][1] == n:
                    n_l = abs(now_l[0]-j)+abs(now_l[1]-1)
                    n_r = abs(now_r[0]-j)+abs(now_r[1]-1)
                    if n_l > n_r:
                        now_r = [j, 1]
                        answer += 'R'
                    elif n_l < n_r:
                        now_l = [j, 1]
                        answer += 'L'
                    else:
                        if hand =="right":
                            now_r = [j, 1]
                            answer += 'R'
                        else:
                            now_l = [j, 1]
                            answer += 'L'
    return answer