import sys
input = sys.stdin.readline

#  시간복잡도 10^4 -> O(nlogn)
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    result = 0
    for i in range(n):
        left, right = 0, m-1
        while left <= right:
            mid = (left+right)//2
            if a[i] <= b[mid]:
                right = mid-1
            elif a[i] > b[mid]:
                left = mid+1
        result += left
    print(result)