import sys
input = sys.stdin.readline

# 시간복잡도 : 10^6 -> 최대 O(logn)
while True:
    n, m = map(int, input().split())
    if n+m == 0:
        break
    # 메모이제이션? no. set
    sanggeun = set()
    ans = 0
    for _ in range(n):
        sanggeun.add(int(input()))
    for _ in range(m):
        seonyeong_now = int(input())
        if seonyeong_now in sanggeun:
            ans += 1
    print(ans)