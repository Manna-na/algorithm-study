import sys
input = sys.stdin.readline

# 시간복잡도 : 10^5 O(N)으로 풀어야
# 1. x기간 동안의 누적합 구하기
# 1-1. end가 start+x보다 작을 동안 누적합 구하기
# 1-2. max_val과 비교
# 2. 큰값 찾기
# 3. 큰값 몇갠지 찾기

n, x = map(int, input().split())
visitors = list(map(int, input().split()))
# 초기 윈도우 설정
current_sum = sum(visitors[:x])
max_sum = current_sum
count = 1

for i in range(x, n):
    # 슬라이딩 윈도우: 오른쪽으로 한 칸 이동
    current_sum += visitors[i] - visitors[i - x]
    # 최대값 갱신
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

# 결과 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)