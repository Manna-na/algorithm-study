import sys
input = sys.stdin.readline

# 조합이에요
while True:
    array = list(map(int, input().split()))
    if array[0] == 0:
        break
    k = array[0]
    nums = array[1:]
    nums.sort()
    selected = [0] * 6
    def recur(cur, start):
        if cur == 6:
            print(*selected)
            return
        for i in range(start, len(nums)):
            selected[cur] = nums[i]
            recur(cur+1, i+1)
    recur(0, 0)
    print()