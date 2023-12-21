import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
deque = deque([i for i in range(1, N+1)])

count = 1
print("<", end="")
while len(deque) > 1:
    deque.rotate(-(K-1))
    print(deque.popleft(), end=", ")
print(deque.popleft(), end=">")