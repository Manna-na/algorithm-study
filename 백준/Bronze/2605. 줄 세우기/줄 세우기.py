import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
answer = []
for i, v in enumerate(array):
    answer.insert(i-v, i+1)
print(*answer)