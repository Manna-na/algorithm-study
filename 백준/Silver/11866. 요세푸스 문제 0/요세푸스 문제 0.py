import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
answer = "<"
while len(queue) > 1:
    for i in range(K-1):
        queue.append(queue.popleft())
    answer += str(queue.popleft()) + ", "
answer += str(queue.popleft()) + ">"
print(answer)