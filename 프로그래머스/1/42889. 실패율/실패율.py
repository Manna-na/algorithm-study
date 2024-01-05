# 1단계 : 각 스테이지에서 클리어하지 못한 사용자 count
# 2단계 : 실패율 구하기 = 스테이지 도달 but, fail player / 스테이지 도달한 플레이어
# 3단계 : 실패율 높은 스테이지부터 내림차순 정렬
# 4단계 : 스테이지 번호 담긴 배열 반환

def solution(N, stages):
    total = len(stages)
    ratio = {}
    for i in range(1, N+1):
        fail = stages.count(i)
        if total > 0:
            ratio[i] = fail / total
        else:
            ratio[i] = 0
        total -= fail
    answer = []
    sorted_ratio = sorted(ratio.items(), key=lambda x:x[1], reverse=True)
    for i in sorted_ratio:
        answer.append(i[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) #[3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) #[4,1,2,3]