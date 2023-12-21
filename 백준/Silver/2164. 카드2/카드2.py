import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
deck = deque(range(1, n+1))
for _ in range(n-1):
    deck.popleft()
    deck.append(deck.popleft())
print(*deck)