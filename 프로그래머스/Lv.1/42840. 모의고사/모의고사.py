# 1단계 : 수포자 패턴 찾기
# 2단계 : 각 패턴으로 문제를 풀 때 몇 개 맞출 수 있는지 체크
# 3단계 : 점수가 가장 큰 수포자 찾기

def solution(answers):
    answer = []
    peoples = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0] * 3

    for i in range(len(peoples)):
        for ans in range(len(answers)):
            if answers[ans] == peoples[i][ans % len(peoples[i])]:
                count[i] += 1
    max_val=max(count)
    for i, v in enumerate(count):
        if v==max_val:
            answer.append(i+1)
    return answer

# print(solution([1, 2, 3, 4, 5])) # [1]
# print(solution([1,3,2,4,2]	)) # [1,2,3]
