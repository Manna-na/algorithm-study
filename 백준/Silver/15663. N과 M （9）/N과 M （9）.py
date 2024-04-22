import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
selected = [0] * m
def recur(cur):
    if cur == m:
        print(*selected)
        return
    last = 0
    for i in range(len(nums)):
        if not visited[i] and last != nums[i]:
            visited[i] = True
            selected[cur] = nums[i]
            recur(cur+1)
            visited[i] = False
            last = nums[i]

recur(0)