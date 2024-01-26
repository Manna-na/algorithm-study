import sys
input = sys.stdin.readline

def binary_search(array_n, target):
    start, end = 0, len(array_n)-1
    while start <= end:
        midIdx = (start+end) // 2
        midValue = array_n[midIdx]
        if midValue > target:
            end = midIdx - 1
        elif midValue < target:
            start = midIdx + 1
        else:
            return True
    return False

N = int(input())
array_n = list(map(int, input().split()))
array_n.sort()

M = int(input())
array_m = list(map(int, input().split()))

for i in range(M):
    target = array_m[i]
    result = binary_search(array_n, target)
    print(1 if result else 0)



