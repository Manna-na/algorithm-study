import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deque = deque()

# 뒤에서 앞으로 가,
# 숫자 추가는 맨 앞에다가
for i in range(n, 0, -1):
    deque.appendleft(i)
    for _ in range(i):
        deque.appendleft(deque.pop())
print(*deque)
