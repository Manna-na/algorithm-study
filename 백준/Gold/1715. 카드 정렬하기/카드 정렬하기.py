import sys
from queue import PriorityQueue

input = sys.stdin.readline
pque = PriorityQueue()

N = int(input())
for _ in range(N):
    pque.put(int(input()))

result = 0
while pque.qsize() > 1:
    x1 = pque.get()
    x2 = pque.get()
    pque.put(x1 + x2)
    result += x1 + x2
    # cnt += 1
    # print(f"{cnt} 일떄 : {x1}, {x2}")

print(result)