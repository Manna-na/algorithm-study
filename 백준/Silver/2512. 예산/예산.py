# 1. 예산 요청 중 최댓값을 상한선, 1을 하한선으로 상한액 찾기
# 2. 예산 요청과 상한액 비교해서 상한액보다 작거나 같으면 요청 금액 그대로
# 3. 상한액보다 크면 상한액 배정
# 4. 배정된 예산의 합을 전체 예산과 비교

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

# 최댓값이 상한선
# 1이 하한선
start, end = 1, max(array)
while start<= end:
    # 배정 예산의 총액이 전체 예산보다 크면 상한액 낮추기
    # 배정 예산의 총액이 전체 예산보다 작거나 같으면 상한액 높이기
    mid = (start+end)//2
    sum_budget = 0
    for r in array:
        sum_budget += min(mid, r)
    if sum_budget > m:
        end = mid - 1
    elif sum_budget <= m:
        start = mid +  1

print(end)