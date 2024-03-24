import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [i for i in range(n+1)]
answer = array
for _ in range(m):
    i, j = map(int, input().split())
    array[j:i-1:-1] = answer[i:j+1]
print(*answer[1:])