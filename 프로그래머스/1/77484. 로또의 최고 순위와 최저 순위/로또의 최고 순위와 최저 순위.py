def solution(lottos, win_nums):
    answer = [0,0]
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
    zero_cnt = lottos.count(0)
    answer[0] = rank[cnt+zero_cnt]
    answer[1] = rank[cnt]
    return answer