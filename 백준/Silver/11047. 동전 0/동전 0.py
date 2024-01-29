import sys
input = sys.stdin.readline

N, K = map(int, input().split())
value_array = [int(input()) for _ in range(N)]
value_array.sort(reverse=True)
result = 0
for val in value_array:
    if val <= K:
        result += K//val
        K %= val
    if K == 0:
        print(result)
        break