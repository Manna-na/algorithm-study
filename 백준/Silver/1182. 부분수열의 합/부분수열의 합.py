import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
# 시간복잡도 O(nlogn)일까나? nono n은 20이야
# 특정조건을 만족하는 부분집합 -> 백트레킹
# 1부터 n개 뽑는 모든 경우의 수를 계산해야해, 조합으로 풀어야 합니다.
# n이 최대 20이니까 가능할 것 같다

ans = 0


def recur(cur, m, start):
    global ans
    if cur == m:
        # print(selected, "sum : ",sum(selected))
        if sum(selected) == s:
            ans += 1
        return
    for i in range(start, n):
        selected[cur] = nums[i]
        recur(cur + 1, m, i + 1)


for i in range(1, n+1):
    selected = [0] * i
    recur(0, i, 0)

print(ans)