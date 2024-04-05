import sys
input = sys.stdin.readline

# 시간복잡도 : 10^5 * 10^5, O(nlogn)
n = int(input())
sanggeun = list(map(int, input().split()))
sanggeun.sort()
m = int(input())
check = list(map(int, input().split()))

result = [0 for _ in range(m)]

for c in range(len(check)):
    start, end = 0, len(sanggeun)-1
    while start <= end:
        mid = (start + end) //  2
        if sanggeun[mid] == check[c]:
            result[c] = 1
            break
        if sanggeun[mid] < check[c]: # mid에 해당하는 값이 내가 찾는애보다 작아
            start = mid + 1
        else:
            end = mid - 1

print(*result, sep=" ")